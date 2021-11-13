from django import conf
from django.shortcuts import render

from .firebase_client import FirebaseClient

from django.conf import settings

from decouple import config, Csv

# Create your views here.
def index(request):
    return render(request, 'index.html')

def list(request):
    client = FirebaseClient()
    docs = client.all()
    context = {
     'docs': [doc.to_dict() for doc in docs]
    }
    return render(request, 'index.html', context)