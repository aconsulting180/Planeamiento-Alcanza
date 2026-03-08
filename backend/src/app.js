require('dotenv').config();
const express = require('express');
const cors = require('cors');
const adminRoutes = require('./routes/admin.routes');

const app = express();

// ── CORS: solo permite el frontend configurado ──
const allowedOrigins = (process.env.FRONTEND_URL || 'http://localhost:5500')
  .split(',').map(o => o.trim());

app.use(cors({
  origin: (origin, callback) => {
    // Permitir peticiones sin origin (Postman, herramientas locales) en dev
    if (!origin || allowedOrigins.includes(origin)) return callback(null, true);
    callback(new Error(`CORS bloqueado para origen: ${origin}`));
  },
  methods: ['GET', 'POST', 'PATCH', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization', 'X-Setup-Token'],
}));

app.use(express.json({ limit: '2mb' }));

// ── Rutas ──
app.use('/admin', adminRoutes);

// ── Health check ──
app.get('/health', (_, res) => {
  res.json({ ok: true, project: 'planeamiento-alcanza-89ed4', ts: new Date().toISOString() });
});

// ── Inicio ──
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`✅ LPS Backend corriendo en http://localhost:${PORT}`);
});
