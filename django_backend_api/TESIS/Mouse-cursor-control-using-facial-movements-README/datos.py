from typing import Any
import time
import threading

class Datos():
    lista = [] #variable de la clase Datos
    
    def __init__(self):
        self.d1 = None
        
    def setattr(self, d1: str) -> str:
        self.d1 = d1
        
    def getattribute(self):
        return self.d1
    
    def set_datosActualizados(self):
        
        Datos.lista.append(self.get_datosVerificados(self.d1))
            
            
    def get_datosActualizados(self):
        return Datos.lista
 
    #metodo para verificar los datos devueltos
    def get_datosVerificados(self, dato1:str) -> str:
        return dato1 if dato1 else "None"







  

