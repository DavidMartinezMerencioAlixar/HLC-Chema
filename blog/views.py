from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saludo(request):
    return HttpResponse("Esta la primera página del blog")

def despedida(request):
    return HttpResponse("Esta es la página de despedida")

