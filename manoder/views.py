from django.shortcuts import render,redirect
import subprocess

# Create your views here.
def home_mano_der(request):
    datos = {
        'titulo': 'Mano derecha',
        'contenido': 'PÁGINA DE GESTOS DE LA MANO DERECHA',
    }
    return render(request, 'manoder/index.html', datos)

def ejecutar_mano_derecha(request):
    # Ruta al script de Python
    script_path = 'C:\TESIS\Virual-Mouse-main\src\Virtual_Mouse.pyw'
    # Ejecutar el script en una terminal
    subprocess.run(['python', script_path])
    return redirect('manoder')  