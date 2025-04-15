from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ArticuloSerializer 
from app_templates.models import Articulo

# Create your views here.
class ArticuloListAPIView(ListAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer 


class ArticuloRetrieveAPIView(RetrieveAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer 

