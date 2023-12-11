import firebase_admin
import os
import json
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

load_dotenv()

data = json.loads(os.getenv("FIREBASE"))
cred = credentials.Certificate(data)
firebase_admin.initialize_app(cred, {'storageBucket': 'estetika-capstone.appspot.com'})
db = firestore.client()
