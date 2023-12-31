from django.urls import path
from recipes import views

# Utilizando app name para passar os nomes das urls no html, para não correr o risco de colisão de nomes
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('recipes/category/<int:category_id>/', views.category, name='category'),
    path('recipes/<int:id>/', views.recipe, name='view-recipe'),
    # Definimos um parâmetro 'id' para essa url e só vai ser aceito se for um 'inteiro', isso trás mais segurança para o código (URL Dinâmica).
]
