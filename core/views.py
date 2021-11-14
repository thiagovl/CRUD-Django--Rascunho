from django.shortcuts import redirect, render
from .firebase_client import FirebaseClient

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Lista todos os dados
def list(request):
    client = FirebaseClient()
    docs = client.all()
    context = {
     'docs': [doc.to_dict() for doc in docs]
    }
    return render(request, 'index.html', context)

# Lista por ID
def list_id(request, id):
    client = FirebaseClient()
    docs = client.get_by_id(id)
    context = {
        'docs': [docs.to_dict()]
    }
    return render(request, 'list_id.html', context)

def vcriar(request):
    return render(request, 'criar.html')

# Inserindo dados
def inserir(request):
    aux = request.POST.get('tags')
    tags = aux.split()
    data = {
        'nome': request.POST.get('nome'),
        'tags': tags
    }

    client = FirebaseClient()

    try:
        print(data)
        client.create(data)
    except Exception as e:
        message = "Ocorreu um erro ao inserir"
        return None
    return redirect('/list/')


def vupdate(request, id):
    client = FirebaseClient()
    docs = client.get_by_id(id)
    context = {
        'docs': [docs.to_dict()]
    }
    return render(request, 'update.html', context)


def update(request, id):
    data = {
        'nome': request.POST.get('nome')
    }
    client = FirebaseClient()
    client.update(id, data)
    return redirect('/list/')

def vdelete(request, id):
    client = FirebaseClient()
    docs = client.get_by_id(id)
    context = {
        'docs': [docs.to_dict()]
    }
    return render(request, 'delete.html', context)

def delete(request, id):
    client = FirebaseClient()
    client.delete_by_id(id)
    return redirect('/list/')

def vfilter(request):
    return render(request, 'vfilter.html')

def filter(request):
    name = request.POST.get('nome')
    client = FirebaseClient()
    docs = client.filter(name)
    
    context = {
        'docs': [doc.to_dict() for doc in docs]
        }
    return render(request, 'filter.html', context)
    

