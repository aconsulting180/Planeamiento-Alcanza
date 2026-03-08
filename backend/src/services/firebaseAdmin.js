const admin = require('firebase-admin');
const path = require('path');

// En Railway: usa la variable de entorno FIREBASE_SERVICE_ACCOUNT (JSON string)
// En local:   usa el archivo serviceAccountKey.json directamente
let credential;

if (process.env.FIREBASE_SERVICE_ACCOUNT) {
  // Producción en Railway
  const serviceAccount = JSON.parse(process.env.FIREBASE_SERVICE_ACCOUNT);
  credential = admin.credential.cert(serviceAccount);
} else {
  // Desarrollo local — usa el archivo
  const keyPath = path.join(__dirname, '../../serviceAccountKey.json');
  credential = admin.credential.cert(require(keyPath));
}

if (!admin.apps.length) {
  admin.initializeApp({ credential });
}

module.exports = admin;
