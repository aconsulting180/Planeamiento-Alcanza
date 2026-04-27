const functions = require('firebase-functions');
const express = require('express');
const cors = require('cors');
const admin = require('firebase-admin');

admin.initializeApp();

const app = express();

const defaultOrigins = [
  'https://aconsulting180.github.io',
  'https://alcanzagrupoinmobiliario.github.io',
  'http://localhost:5500',
  'http://127.0.0.1:5500'
];

const allowedOrigins = (process.env.FRONTEND_URL || defaultOrigins.join(','))
  .split(',')
  .map((o) => o.trim())
  .filter(Boolean);

app.use(cors({
  origin: (origin, callback) => {
    if (!origin || allowedOrigins.includes(origin)) {
      return callback(null, true);
    }
    return callback(new Error(`CORS bloqueado para origen: ${origin}`));
  },
  methods: ['GET', 'POST', 'PATCH', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization', 'X-Setup-Token']
}));

app.use(express.json({ limit: '2mb' }));

async function requireAuth(req, res, next) {
  const authHeader = req.headers.authorization;
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'No autorizado: falta el token.' });
  }

  try {
    const token = authHeader.split('Bearer ')[1];
    req.user = await admin.auth().verifyIdToken(token);
    return next();
  } catch (_) {
    return res.status(401).json({ error: 'Token invalido o expirado.' });
  }
}

const requireAdmin = [
  requireAuth,
  (req, res, next) => {
    if (req.user.role !== 'admin') {
      return res.status(403).json({ error: 'Acceso denegado: se requiere rol admin.' });
    }
    return next();
  }
];

app.get('/admin/users', requireAdmin, async (req, res) => {
  try {
    const listResult = await admin.auth().listUsers(1000);
    const users = await Promise.all(listResult.users.map(async (u) => {
      let profile = {};
      try {
        const doc = await admin.firestore().collection('users').doc(u.uid).get();
        if (doc.exists) {
          profile = doc.data();
        }
      } catch (_) {
      }

      return {
        uid: u.uid,
        email: u.email,
        displayName: u.displayName || profile.displayName || '',
        role: (u.customClaims && u.customClaims.role) || profile.role || 'user',
        active: !u.disabled,
        disabled: !!u.disabled,
        createdAt: u.metadata.creationTime,
        creationTime: u.metadata.creationTime,
        photoURL: u.photoURL || ''
      };
    }));

    return res.json(users);
  } catch (e) {
    return res.status(500).json({ error: e.message });
  }
});

app.post('/admin/users', requireAdmin, async (req, res) => {
  const { email, password, displayName, role } = req.body;

  if (!email || !password || !role) {
    return res.status(400).json({ error: 'email, password y role son requeridos.' });
  }

  if (!['admin', 'user'].includes(role)) {
    return res.status(400).json({ error: 'role debe ser "admin" o "user".' });
  }

  try {
    const user = await admin.auth().createUser({
      email,
      password,
      displayName: displayName || ''
    });

    await admin.auth().setCustomUserClaims(user.uid, { role });
    await admin.firestore().collection('users').doc(user.uid).set({
      email,
      displayName: displayName || '',
      role,
      active: true,
      createdAt: new Date().toISOString(),
      createdBy: req.user.email || 'system'
    });

    return res.status(201).json({ success: true, uid: user.uid });
  } catch (e) {
    return res.status(400).json({ error: e.message });
  }
});

app.patch('/admin/users/:uid/role', requireAdmin, async (req, res) => {
  const { role } = req.body;

  if (!['admin', 'user'].includes(role)) {
    return res.status(400).json({ error: 'role debe ser "admin" o "user".' });
  }

  try {
    await admin.auth().setCustomUserClaims(req.params.uid, { role });
    await admin.firestore().collection('users').doc(req.params.uid).set({
      role,
      updatedAt: new Date().toISOString(),
      updatedBy: req.user.email || 'system'
    }, { merge: true });

    return res.json({ success: true });
  } catch (e) {
    return res.status(400).json({ error: e.message });
  }
});

app.patch('/admin/users/:uid/status', requireAdmin, async (req, res) => {
  const { active } = req.body;

  if (typeof active !== 'boolean') {
    return res.status(400).json({ error: 'active debe ser true o false.' });
  }

  try {
    await admin.auth().updateUser(req.params.uid, { disabled: !active });
    await admin.firestore().collection('users').doc(req.params.uid).set({
      active,
      updatedAt: new Date().toISOString(),
      updatedBy: req.user.email || 'system'
    }, { merge: true });

    return res.json({ success: true });
  } catch (e) {
    return res.status(400).json({ error: e.message });
  }
});

app.post('/admin/users/:uid/reset-password', requireAdmin, async (req, res) => {
  try {
    const user = await admin.auth().getUser(req.params.uid);
    const link = await admin.auth().generatePasswordResetLink(user.email);
    return res.json({ success: true, resetLink: link });
  } catch (e) {
    return res.status(400).json({ error: e.message });
  }
});

app.post('/admin/set-first-admin', async (req, res) => {
  const setupToken = req.headers['x-setup-token'];
  if (!setupToken || setupToken !== process.env.SETUP_TOKEN) {
    return res.status(403).json({ error: 'Setup token invalido.' });
  }

  const { uid } = req.body;
  if (!uid) {
    return res.status(400).json({ error: 'uid requerido.' });
  }

  try {
    await admin.auth().setCustomUserClaims(uid, { role: 'admin' });
    await admin.firestore().collection('users').doc(uid).set({
      role: 'admin',
      active: true,
      updatedAt: new Date().toISOString(),
      note: 'Primer admin asignado via setup'
    }, { merge: true });

    return res.json({ success: true, message: `UID ${uid} ahora es admin.` });
  } catch (e) {
    return res.status(400).json({ error: e.message });
  }
});

app.get('/health', (_, res) => {
  res.json({ ok: true, provider: 'firebase-functions', ts: new Date().toISOString() });
});

exports.api = functions.https.onRequest(app);
