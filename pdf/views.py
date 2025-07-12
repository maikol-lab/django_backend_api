from django.shortcuts import render
from django.http import FileResponse
import mimetypes
import os

# Create your views here.
def home(request):
    return render(request, 'pdf/index.html')

def descargar_pdf(request):
    filename = 'MANUAL DE USUARIO.pdf'
    
    file_path = f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/descargas/{filename}'
    mime_type, _ = mimetypes.guess_type(file_path)
    
    response = FileResponse(open(file_path, 'rb'), content_type = mime_type)
    response['Content-Disposition'] = f"attachment; filename={filename}"
    
    return response

def ver_pdf(request):
    filename = 'MANUAL DE USUARIO.pdf'
    
    file_path = f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/descargas/{filename}'
    mime_type, _ = mimetypes.guess_type(file_path)
    
    response = FileResponse(open(file_path, 'rb'), content_type = mime_type)
    response['Content-Disposition'] = f"inline; filename={filename}"
    
    return response