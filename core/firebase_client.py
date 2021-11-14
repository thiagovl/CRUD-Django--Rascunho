from django.utils.functional import empty
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from django.conf import settings

class FirebaseClient:

    
    def __init__(self):

        if not firebase_admin._apps: # Necessário para que não conecte novamente
            cred = credentials.Certificate(
                settings.FIREBASE_ADMIN_CERT # Importa a variável que contém os dados de conexão
            )
            firebase_admin.initialize_app(cred)
        

        self._db = firestore.client()
        self._collection = self._db.collection('evento') # evento é o nome da coleção
  
    # Busca todos os dados da coleção evento
    def all(self):
        """Get all todo from firestore database"""
        docs = self._collection.get()

        return docs #[{**doc.to_dict(), "nome": doc.nome} for doc in docs]

    # Retornando pelo ID
    def get_by_id(self, id):
        """Get todo on firestore database using document id"""
        doc_ref = self._collection.document(id)
        doc = doc_ref.get()

        if doc.exists:
            return doc #{**doc.to_dict(), "nome": doc.id}
        return
        
    # Inserindo dados
    def create(self, data):
        """Create todo in firestore database"""
        doc_ref = self._collection.document()
        id = doc_ref.id
        data = {
            'id': id,
            'nome': data['nome']
        }
        doc_ref.set(data)
        
    # Atualizando dados
    def update(self, id, data):
        """Update todo on firestore database using document id"""
        doc_ref = self._collection.document(id)
        doc_ref.update(data)
    
    # Deletando dados
    def delete_by_id(self, id):
        """Delete todo on firestore database using document id"""
        self._collection.document(id).delete()

    # Listando consulta
    def filter(self, name):

        
        docs = self._collection.where("nome", ">=", name).get()
        if not docs:
            docs = self._collection.where("nome", "<=", name).get()
        # docs = self._collection.where('nome', '=', 'Criado agora')
        # if docs.exists:
        #     return docs #{**doc.to_dict(), "nome": doc.id}
        # for doc in docs:
        #     print(doc.to_dict())

        return docs