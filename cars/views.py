# importando a lib render, que renderiza no navegador o html dos templates
from django.shortcuts import render
from cars.models import Car

# respota do get na url
# busca o html de render
def cars_view(request):
     print(request.GET.get('search')) # pega a requisicao get do usuario n0 valor -- /search

     #aqui, o "ID" representa o id da marca, se quiser buscar por nome, deve usar -> brand__name <- # busca todos os modelos de carros - querySet
     cars = Car.objects.all() #ID por ordem de criaçao (id=1) ou name 
    
     # request da url, e o caminho do nosso html
     return render(request, 'cars.html', {'cars': cars } ) # passando os modelos de carros na pagina web
