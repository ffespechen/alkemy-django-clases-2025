from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone


# Create your views here.
def bienvenida(request):
    return HttpResponse(content="Hola desde Django Alkemy!")


def saludar(request, nombre):
    return HttpResponse(content=F"Hola a Django Alkemy {nombre.upper()}")


def cumpleanio(request, anio, mes, dia):
    return HttpResponse(content=f'La fecha de cumpleaños es {dia}/{mes}/{anio}')


def mensaje_html(request):
    html = F'''
    <html>
        <body>
            <h1>Hola soy HTML</h1>
            <h2>{timezone.now()}</h2>
        </body>
    </html>
            '''
    return HttpResponse(content=html)