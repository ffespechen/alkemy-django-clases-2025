from django.db import models

# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    activo = models.BooleanField(default=True)
    promocion = models.BooleanField(default=False)

    def __str__(self):
        return F"{self.nombre.upper()} $ {self.precio} [ {self.cantidad} ]"
    
    class Meta:
        ordering = ['nombre']