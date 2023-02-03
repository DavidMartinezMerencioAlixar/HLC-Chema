from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Articulo

import datetime

# Create your views here.
class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request):
    #persona = Persona("Chema", "Durán")
    #fecha_actual = datetime.datetime.now()
    #return render(request, "saludo.html", {"nombre_persona":persona.nombre, "apellido_persona":persona.apellido, "fecha_actual":fecha_actual})
    persona = Persona("Chema", "Durán")
    temas_del_curso = ["Formularios", "Modelos", "Vistas", "Despliegue"]
    fecha_actual = datetime.datetime.now()
    return render(request, "saludo.html",
        {"nombre_persona": persona.nombre,
        "apellido_persona": persona.apellido,
        "fecha_actual": fecha_actual,
        "temas" : temas_del_curso})

def despedida(request):
    return HttpResponse("Esta es la página de despedida")

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    
    documento = """
    <html>
    <body>
    <h2>
    La fecha y hora actual es: {}
    </h2>
    </body>
    </html>
    """.format(fecha_actual)

    return HttpResponse(documento)

def calculaEdadActual(request, edad, agno):
    periodo = agno - datetime.datetime.now().year 
    nueva_edad = edad + periodo
    documento = """
    <html>
    <body>
    <h2>
    En el año {} tendrás: {}
    </h2>
    </body>
    </html>
    """.format(agno, nueva_edad)

    return HttpResponse(documento)

def curso_django(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "curso_django.html", {"fecha_actual": fecha_actual})

def curso_python(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "curso_python.html", {"fecha_actual": fecha_actual})

def crear_articulo(request, nombre, seccion, precio):
    articulo = Articulo.crear_articulo(nombre, seccion, precio)
    return render(request, "crear_articulo.html", {"articulo": articulo})

def mostrar_articulos(request):
    articulos = Articulo.todos_articulos()
    return render(request, "mostrar_articulos.html", {"articulos": articulos})

def borrar_articulo(request, id):
    articulo = Articulo.borrar_articulo(id)
    return render(request, "borrar_articulo.html", {"id_articulo": id})

def actualizar_articulo(request, id, nombre, seccion, precio):
    articulo = Articulo.actualizar_articulo(id, nombre, seccion, precio)
    return render(request, "actualizar_articulo.html", {"articulo": articulo})
