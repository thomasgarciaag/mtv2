from django.shortcuts import render
from django.http import HttpResponse
from aplicacion.models import bd_familiares
from django.template import Template, Context

# Create your views here.

def listado_familiares(request):
    familiares = bd_familiares.objects.all()

    cadena_respuesta = []
    for familiar in familiares:
        cadena_respuesta += familiar.nombre ," ", familiar.edad ,  " | " 

    datos = {"listado_familiares" : familiares}

    contexto = Context(datos)
    
    return HttpResponse(cadena_respuesta)    

    


