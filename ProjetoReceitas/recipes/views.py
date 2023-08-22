from django.shortcuts import render

# Create your views here.
def home(request):
    utils = {
        'title': 'HomePage',
    }

    return render(request, 'index.html', context=utils)