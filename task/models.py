from django.db import models

# Create your models here.
class Datos_Facial(models.Model):

    titulo = models.CharField(max_length=100)
    dato_1 = models.CharField(max_length=100)
    dato_2 = models.CharField(max_length=100)
    dato_3 = models.CharField(max_length=100)
    dato_4 = models.CharField(max_length=100)
    dato_5 = models.CharField(max_length=100)




