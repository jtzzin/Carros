# importando a lib render, que renderiza no navegador o html dos templates
from django.shortcuts import render

# respota do get na url
# busca o html de render
def cars_view(request):
     # request da url, e o caminho do nosso html
     return render(request, 'cars.html', {'cars': {'model': 'santana 1.8'} } )
