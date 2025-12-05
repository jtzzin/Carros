# importacao de modulos
from django.contrib import admin
from cars.models import Car, Brand

# Register your models here.
#list_display mostra os campos do painel, search_fields é poelo modelo que vai ser buscado
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    # buscando pela modelo do carro
    search_fields = ('model', 'brand')

class BrandAdmin(admin.ModelAdmin):
    # Adicionando marcas no sistema e buscando pelos nomes, essa classe liga na outra
    list_display = ("name",)
    search_fields = ("name",)

# dizendo ao django para colocar isso no sistema
admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)