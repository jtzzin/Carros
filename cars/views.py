# importando a lib render, que renderiza no navegador o html dos templates
from django.shortcuts import render
from cars.models import Car

# respota do get na url
# busca o html de render
def cars_view(request):
     # se bater na rota /cars padrao
     cars = Car.objects.all().order_by("model") # retorna todos os carros e retorna por ordem alfabetica. se eu colcoar -model, ele faz do Z ao A

     #capturando a requisicao via url /search=
     search = request.GET.get("search")
     
     if search: # verificando se esta com o campo
          #aqui, poderia ser "ID" representando o id da marca, se quiser buscar por nome, deve usar -> brand__name <- # busca todos os modelos de carros - querySet
          cars = Car.objects.filter(model__icontains=search) #retornando o model do carro, "icontains" ignora regra de minusculas e maiusculas. "order_by" ordena por campo do banco

     # request da url, e o caminho do nosso html
     return render(
          request,
          'cars.html',
          {'cars': cars } 
     ) # passando os modelos de carros na pagina web
