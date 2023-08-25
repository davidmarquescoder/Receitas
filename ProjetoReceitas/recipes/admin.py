from django.contrib import admin
from .models import Category, Recipe

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)

'''
Para regitrar um model precisamos criar uma classe para o model e precisamos registrar ele.
Para isso podemos utilizar dois métodos diferentes, o primeiro deles, é o método realizado a cima
com o "admin.site.register(ClasseDoModel, ClasseDoModelAdmin)" e o segundo método é o realizado abaixo,
usando decorator "@admin.register(ClasseDoModel)". As classe criadas aqui nesse arquivo, vão servir para
passarmos configurações para esses bancos lá na página de admin.
'''

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...