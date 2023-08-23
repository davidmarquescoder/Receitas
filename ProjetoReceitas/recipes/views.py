from django.shortcuts import render

# Create your views here.
def home(request):
    utils = {
        'title': 'HomePage',
        'nome': 'David Marques',
    }

    return render(request, 'recipes/pages/index.html', context=utils)

# O parâmetro 'id' deve ser obrigatoriamente passado aqui na view.
def recipe(request, id):
    utils = {
        'title': 'Receitas',
        'nome': 'David Marques',
    }

    return render(request, 'recipes/pages/recipe-view.html', context=utils)