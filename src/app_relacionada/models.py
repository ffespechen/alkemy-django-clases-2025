from django.db import models
from app_templates.models import Articulo

# Create your models here.
class Relacionado(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    leyenda = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return F"{self.id} - {self.fecha}"