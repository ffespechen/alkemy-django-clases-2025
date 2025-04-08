from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.Articulo)

@admin.register(models.Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'cantidad', 'activo', 'promocion']
    list_filter  = ['activo', 'precio']
    search_fields = ['nombre']