from django.urls import path
from . import views

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("saludar", views.saludar),
    path('saludo/<str:nombre>/', views.saludar_usuario),
    path('edad/<int:edad>/', views.mostrar_edad),
    path("curriculum/", views.curriculum, name="curriculum"),
    path("position/", views.position, name="position"),
]