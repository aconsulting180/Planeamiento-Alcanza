const express = require('express');
const admin = require('../services/firebaseAdmin');
const requireAdmin = require('../middleware/requireAdmin');
const router = express.Router();

// ──────────────────────────────────────────────────────────
// GET /admin/users — Listar todos los usuarios
// ──────────────────────────────────────────────────────────
router.get('/users', requireAdmin, async (req, res) => {
  try {
    const listResult = await admin.auth().listUsers(100);
    const users = await Promise.all(listResult.users.map(async u => {
      let profile = {};
      try {
        const doc = await admin.firestore().collection('users').doc(u.uid).get();
        if (doc.exists) profile = doc.data();
      } catch (_) {}
      return {
        uid: u.uid,
        email: u.email,
        displayName: u.displayName || profile.displayName || '',
        role: (u.customClaims && u.customClaims.role) || profile.role || 'user',
        active: !u.disabled,
        createdAt: u.metadata.creationTime,
        photoURL: u.photoURL || '',
      };
    }));
    res.json(users);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

// ──────────────────────────────────────────────────────────
// POST /admin/users — Crear nuevo usuario
// ──────────────────────────────────────────────────────────
router.post('/users', requireAdmin, async (req, res) => {
  const { email, password, displayName, role } = req.body;
  if (!email || !password || !role) {
    return res.status(400).json({ error: 'email, password y role son requeridos.' });
  }
  if (!['admin', 'user'].includes(role)) {
    return res.status(400).json({ error: 'role debe ser "admin" o "user".' });
  }
  try {
    const user = await admin.auth().createUser({ email, password, displayName: displayName || '' });
    await admin.auth().setCustomUserClaims(user.uid, { role });
    await admin.firestore().collection('users').doc(user.uid).set({
      email,
      displayName: displayName || '',
      role,
      active: true,
      createdAt: new Date().toISOString(),
      createdBy: req.user.email,
    });
    res.status(201).json({ success: true, uid: user.uid });
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

// ──────────────────────────────────────────────────────────
// PATCH /admin/users/:uid/role — Cambiar rol
// ──────────────────────────────────────────────────────────
router.patch('/users/:uid/role', requireAdmin, async (req, res) => {
  const { role } = req.body;
  if (!['admin', 'user'].includes(role)) {
    return res.status(400).json({ error: 'role debe ser "admin" o "user".' });
  }
  try {
    await admin.auth().setCustomUserClaims(req.params.uid, { role });
    await admin.firestore().collection('users').doc(req.params.uid)
      .update({ role, updatedAt: new Date().toISOString(), updatedBy: req.user.email });
    res.json({ success: true });
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

// ──────────────────────────────────────────────────────────
// PATCH /admin/users/:uid/status — Activar / desactivar
// ──────────────────────────────────────────────────────────
router.patch('/users/:uid/status', requireAdmin, async (req, res) => {
  const { active } = req.body;
  if (typeof active !== 'boolean') {
    return res.status(400).json({ error: 'active debe ser true o false.' });
  }
  try {
    await admin.auth().updateUser(req.params.uid, { disabled: !active });
    await admin.firestore().collection('users').doc(req.params.uid)
      .update({ active, updatedAt: new Date().toISOString() });
    res.json({ success: true });
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

// ──────────────────────────────────────────────────────────
// POST /admin/users/:uid/reset-password — Generar link de reset
// ──────────────────────────────────────────────────────────
router.post('/users/:uid/reset-password', requireAdmin, async (req, res) => {
  try {
    const user = await admin.auth().getUser(req.params.uid);
    const link = await admin.auth().generatePasswordResetLink(user.email);
    res.json({ success: true, resetLink: link });
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

// ──────────────────────────────────────────────────────────
// POST /admin/set-first-admin — Asignar primer admin (uso único)
// Protegido con un token secreto en header X-Setup-Token
// ──────────────────────────────────────────────────────────
router.post('/set-first-admin', async (req, res) => {
  const setupToken = req.headers['x-setup-token'];
  if (!setupToken || setupToken !== process.env.SETUP_TOKEN) {
    return res.status(403).json({ error: 'Setup token inválido.' });
  }
  const { uid } = req.body;
  if (!uid) return res.status(400).json({ error: 'uid requerido.' });
  try {
    await admin.auth().setCustomUserClaims(uid, { role: 'admin' });
    await admin.firestore().collection('users').doc(uid).set({
      role: 'admin', active: true,
      updatedAt: new Date().toISOString(),
      note: 'Primer admin asignado via setup'
    }, { merge: true });
    res.json({ success: true, message: `UID ${uid} ahora es admin.` });
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

module.exports = router;
