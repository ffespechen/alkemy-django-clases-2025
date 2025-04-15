from rest_framework.serializers import ModelSerializer
from app_templates.models import Articulo

class ArticuloSerializer(ModelSerializer):
    class Meta:
        model = Articulo
        fields = ['nombre', 'precio', 'cantidad', 'activo', 'promocion']