from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saludar(request):
    return HttpResponse("Hola, mi web de Django")

def saludar_usuario(request, nombre):
    return HttpResponse(f"Hola, {nombre}!") 

def mostrar_edad(request, edad):
    return HttpResponse(f"Tu edad es: {edad} años.")

def inicio(request):
    contexto = {"nombre": "Usuario"}
    return render(request, "mi_web/index.html", contexto)

def curriculum(request):
    mensaje = ""
    if request.method == "POST":
        email = request.POST.get("encuesta_email")
        recibir = request.POST.get("recibir_correos")
        como = request.POST.get("como_supo")
        mensaje = "¡Gracias por responder la encuesta!"
    return render(request, "mi_web/cv.html", {"mensaje": mensaje})

def position(request):
    return render(request, "mi_web/position.html")

