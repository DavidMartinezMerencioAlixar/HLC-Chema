from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        print(self)

class Articulos(models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.CharField(max_length=10)
    precio = models.CharField(max_length=10)

    def __str__(self):
        print(self)

class Pedidos(models.Model):
    numero = models.CharField(max_length=10)
    fecha = models.CharField(max_length=20)
    entregado = models.CharField(max_length=1)

    def __str__(self):
        print(self)
        