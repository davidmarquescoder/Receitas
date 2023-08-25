from django.shortcuts import render
from utils.testing.factory import make_recipe

# Create your views here.
def home(request):
    utils = {
        'title': 'HomePage',
        'nome': 'David Marques',
        'receitas': [make_recipe() for _ in range(9)],
    }

    return render(request, 'recipes/pages/index.html', context=utils)

# O parâmetro 'id' deve ser obrigatoriamente passado aqui na view.
def recipe(request, id):
    utils = {
        'title': 'Receita',
        'nome': 'David Marques',
        'receita': make_recipe(),
        'is_detail_page': True,
    }

    return render(request, 'recipes/pages/recipe-view.html', context=utils)