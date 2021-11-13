import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from django.conf import settings
from decouple import config, Csv

class FirebaseClient:

    
    def __init__(self):
        cred = credentials.Certificate({
            settings.FIREBASE_ADMIN_CERT
        })
        firebase_admin.initialize_app(cred)
        

        self._db = firestore.client()
        self._collection = self._db.collection('evento')
  
    def all(self):
        """Get all todo from firestore database"""
        docs = self._collection.get()
        return docs #[{**doc.to_dict(), "nome": doc.nome} for doc in docs]


    