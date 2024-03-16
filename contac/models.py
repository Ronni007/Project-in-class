from django.db import models
from datetime import date


# Create your models here.


class empleado(models.Model):
  name = models.CharField(max_length=30, null=True)
  apellido = models.CharField(max_length=30, null=True)
  mail = models.EmailField(max_length=40,)
  telefono = models.IntegerField()
  mail = models.EmailField(max_length=40,)
  direccion = models.CharField(max_length=40)

  


class contac(models.Model):
  cargo = models.CharField(max_length= 40)
  tareas = models.CharField(max_length=40)
  id_empleado = models.ForeignKey(empleado, on_delete=models.CASCADE, null=True, blank=True)