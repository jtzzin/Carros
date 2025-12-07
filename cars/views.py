# importando a lib render, que renderiza no navegador o html dos templates
from django.shortcuts import render
from cars.models import Car

# respota do get na url
# busca o html de render
def cars_view(request):
     cars = Car.objects.all() # busca todos os modelos de carros - querySet
    
     # request da url, e o caminho do nosso html
     return render(request, 'cars.html', {'cars': cars } ) # passando os modelos de carros na pagina web
