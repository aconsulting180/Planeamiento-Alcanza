const admin = require('../services/firebaseAdmin');

/**
 * Middleware: verifica que la petición tenga un ID token válido de Firebase.
 * Agrega req.user con los datos del token decodificado.
 */
module.exports = async (req, res, next) => {
  const authHeader = req.headers.authorization;
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'No autorizado: falta el token.' });
  }
  try {
    const token = authHeader.split('Bearer ')[1];
    req.user = await admin.auth().verifyIdToken(token);
    next();
  } catch (e) {
    return res.status(401).json({ error: 'Token inválido o expirado.' });
  }
};
