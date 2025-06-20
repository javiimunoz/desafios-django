from django.http import HttpResponse

def saludar(request):
    return HttpResponse("Hola, mi web de Django")

def saludo_personalizado(request, nombre):
    return HttpResponse(f"Hola, {nombre}! Qué tal?")

def mostrar_edad(request, edad):
    return HttpResponse(f"Tu edad es: {edad} años.")