from django.shortcuts import render,redirect
import subprocess

# Create your views here.
def home_mano_izq(request):
    datos = {
        'titulo': 'Mano izquierda',
        'contenido': 'PÁGINA DE GESTOS DE LA MANO IZQUIERDA',
    }
    return render(request, 'manoizq/index.html', datos)

def ejecutar_mano_izquierda(request):
    # Ruta al script de Python
    script_path = 'C:\TESIS\Virual-Mouse-main\src\Virtual_Mouse_izquierda.pyw'
    # Ejecutar el script en una terminal
    subprocess.run(['python', script_path])
    return redirect('manoizq')