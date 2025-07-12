from django.shortcuts import render, redirect
from django.http import HttpResponse
from imutils import face_utils
import numpy as np
import subprocess
import sys

# Create your views here.
# Esta es la Función de inicio de la Aplicación. llama la funcion "index-html"
def home_facial(request): 
    datos = { # Diccionario de datos que debo pasarle a la PLANTILLA.
        'titulo': 'Facial',
        'contenido': 'PÁGINA DE GESTOS FACIALES'  
    }
    # despues Renderizo la Platilla, que es la respuesta que se se esta pasando a la plantilla que es el index.html
    return render(request, 'facial/index.html', datos)

def ejecutar_facial(request):
    # Ruta al script de Python
    script_path = 'c:/tesis/Mouse-cursor-control-using-facial-movements-README/mouse-cursor-control.pyw'
    # Ejecutar el script en una terminal
    subprocess.run(['python', script_path])

    return redirect('facial')
    
def detener_facial(request):
    sys.exit()
    