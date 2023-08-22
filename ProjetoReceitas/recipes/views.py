from django.shortcuts import render

# Create your views here.
def home(request):
    utils = {
        'title': 'HomePage',
        'nome': 'David Marques',
    }

    return render(request, 'recipes/pages/index.html', context=utils)