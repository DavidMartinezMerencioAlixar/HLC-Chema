from django.shortcuts import render
from django.http import HttpResponse

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
        {"nombre_persona":persona.nombre,
        "apellido_persona":persona.apellido,
        "fecha_actual":fecha_actual,
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
