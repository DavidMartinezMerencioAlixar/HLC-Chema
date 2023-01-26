from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre completo del cliente")
    direccion = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=7)
    movil = models.CharField(max_length=9, null=True)

    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.CharField(max_length=10)
    precio = models.FloatField()

    def __str__(self):
        return '{} y su precio es {}'.format(self.nombre, self.precio)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return "Pedido {} entregado: {}".format(self.numero, self.entregado)
