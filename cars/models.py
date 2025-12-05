from django.db import models

# criando os models do banco de dados
# tabela de marcas e carros
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') # protecao contra delete de usuario
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to="cars/", blank=True, null=True)
    


    # retira frases object padrao do django, retornando apenas o model (modelo) dos carros
    def __str__(self):
        return self.model
    



"""
--------------------------------------------------------------------------------------------------------------------------------------------
Importante:
--------------------------------------------------------------------------------------------------------------------------------------------
sempre que alterar os models, rodar o python manage.py makemigrations e migrate"
tambem devemos mudar o admnin.py

para transformar esse modelo em uma tabela no banco de dados, usamos o comando: python manage.py makemigrations e python manage.py migrate, 
fazendo esse comando rodar um script que cria uma tabela sql


"""  
 


