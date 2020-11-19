from django.db import models

# Create your models here.
class Area(models.Model):
    nombre = models.CharField(max_length=200)
    apellido= models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    email= models.CharField(max_length=200)