from django.shortcuts import render, get_list_or_404
from utils.testing.factory import make_recipe
from recipes.models import Recipe
#from django.http import Http404

# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    utils_1 = {
        'title': 'HomePage',
        'nome': 'David Marques',
        'receitas': recipes,
    }

    return render(request, 'recipes/pages/index.html', context=utils_1)

def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
        )

    # Aula 63 da seção 8'
    #if not recipes:
    #    raise Http404('Not Found 😥')

    utils_2 = {
        # recipes.first().category.name - Foi necessário alterar para usar o get_list_or_404, pois essa função retorna uma lista
        'title': f'{recipes[0].category.name} | Categoria Receita',
        'nome': 'David Marques',
        'receitas': recipes,
    }

    return render(request, 'recipes/pages/index.html', context=utils_2)

# O parâmetro 'id' deve ser obrigatoriamente passado aqui na view.
def recipe(request, id):
    utils_3 = {
        'title': 'Receita',
        'nome': 'David Marques',
        'receitas': make_recipe(),
        'is_detail_page': True,
    }

    return render(request, 'recipes/pages/recipe-view.html', context=utils_3)