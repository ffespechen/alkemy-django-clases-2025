from rest_framework.serializers import ModelSerializer
from app_templates.models import Articulo
from app_relacionada.models import Relacionado

class ArticuloSerializer(ModelSerializer):
    class Meta:
        model = Articulo
        fields = ['pk', 'nombre', 'precio', 'cantidad', 'activo', 'promocion']


class RelacionadoSerializer(ModelSerializer):
    class Meta:
        model = Relacionado
        fields = ['pk', 'articulo', 'leyenda', 'fecha']