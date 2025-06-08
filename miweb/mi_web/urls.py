from django.urls import path
from . import views

urlpatterns = [
    path("saludar", views.saludar), #de prueba
    path('saludo/<str:nombre>/', views.saludar_usuario), #Ruta con texto
    path('edad/<int:edad>/', views.mostrar_edad), #Ruta con numero
]