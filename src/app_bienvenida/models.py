from django.db import models

# Create your models here.
class Persona(models.Model):
    apellido = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    dni = models.PositiveBigIntegerField()
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return F"Persona {self.apellido}, {self.nombre} [ {self.dni} ]"