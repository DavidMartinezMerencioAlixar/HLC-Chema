from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre completo del cliente")
    direccion = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=7)
    movil = models.CharField(max_length=9, null=True)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.CharField(max_length=10)
    precio = models.FloatField()

    def crear_articulo(p_nombre, p_seccion, p_precio):
        art = Articulo.objects.create(nombre=p_nombre, seccion=p_seccion, precio=p_precio)
        art.save()
        return art

    def todos_articulos():
        todos = Articulo.objects.all()
        return todos
    
    def borrar_articulo(p_id):
        Articulo.objects.get(id=p_id).delete()
    
    def actualizar_articulo(p_id, p_nombre, p_seccion, p_precio):
        art = Articulo.objects.get(id=p_id)
        art.nombre = p_nombre
        art.seccion = p_seccion
        art.precio = p_precio
        art.save()
        return art

    def __str__(self):
        return '{} y su precio es {}'.format(self.nombre, self.precio)

class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return "Pedido {} entregado: {}".format(self.numero, self.entregado)
