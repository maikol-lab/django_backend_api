from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='inicio-pdf'),
    path('descargar/', views.descargar_pdf, name='manual-pdf'),
    path('ver/', views.ver_pdf, name='ver-manual-pdf'),
]