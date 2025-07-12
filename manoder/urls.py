from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_mano_der, name='manoder'),
    path('exemanoder', views.ejecutar_mano_derecha, name='exemanoder'),
]