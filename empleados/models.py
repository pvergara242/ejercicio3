from django.db import models
from managers.models import Manager
from areas.models import Area


# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)

    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    managers = models.ManyToManyField(Manager, related_name='empleados')