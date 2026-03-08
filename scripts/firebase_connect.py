from pathlib import Path
import firebase_admin
from firebase_admin import credentials, firestore

BASE_DIR = Path(__file__).resolve().parent.parent
cred_path = BASE_DIR / "backend" / "serviceAccountKey.json"

cred = credentials.Certificate(cred_path)

firebase_admin.initialize_app(cred)

db = firestore.client()

print("Firebase conectado correctamente")