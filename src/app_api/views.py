from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly 
from .serializers import ArticuloSerializer, RelacionadoSerializer
from app_templates.models import Articulo
from app_relacionada.models import Relacionado


# Create your views here.
class ArticuloListCreateAPIView(ListCreateAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer 


class ArticuloRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer 


class RelacionadoViewSet(viewsets.ModelViewSet):
    queryset = Relacionado.objects.all()
    serializer_class = RelacionadoSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, ]