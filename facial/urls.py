#Importamos la libreria del modulo url
from django.urls import path # Aqui me permite establecer el modulo Rutas
from . import views # aqui estoy importando mi modulo vistas.

# Aqui contiene todas las rutas que va a tener l aplicación
urlpatterns = [
    path('', views.home_facial, name='facial'), # Ruta Home Facial
    path('exefacial/', views.ejecutar_facial, name='exefacial'), # Ruta ejecuta facial
    path('detenerfacial/', views.ejecutar_facial, name='detenerfacial'), # ruta detener facial
]