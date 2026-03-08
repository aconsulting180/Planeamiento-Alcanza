const requireAuth = require('./requireAuth');

/**
 * Middleware: verifica que el usuario autenticado tenga rol 'admin'
 * (via custom claim). Debe usarse después de requireAuth.
 */
module.exports = [
  requireAuth,
  (req, res, next) => {
    if (req.user.role !== 'admin') {
      return res.status(403).json({ error: 'Acceso denegado: se requiere rol admin.' });
    }
    next();
  }
];
