from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saludar(request):
    return HttpResponse("Hola, mi web de Django")

def saludar_usuario(request, nombre):
    return HttpResponse(f"Hola, {nombre}!") 

def mostrar_edad(request, edad):
    return HttpResponse(f"Tu edad es: {edad} años.")