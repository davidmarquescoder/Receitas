from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.home),
    # Definimos um parâmetro 'id' para essa url e só vai ser aceito se for um 'inteiro', isso trás mais segurança para o código (URL Dinâmica).
    path('recipes/<int:id>/', views.recipe),
]
