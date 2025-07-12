from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_mano_izq, name='manoizq'),
    path('exemanoizq', views.ejecutar_mano_izquierda, name='exemanoizq'),
]