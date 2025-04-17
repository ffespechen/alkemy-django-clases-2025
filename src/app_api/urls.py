from django.urls import path 
from .views import (
    ArticuloListCreateAPIView,
    ArticuloRetrieveUpdateDestroyAPIView

)

app_name = 'app_api'

urlpatterns = [
    path('', ArticuloListCreateAPIView.as_view(), name='listar_crear_api'),
    path('<int:pk>/', ArticuloRetrieveUpdateDestroyAPIView.as_view(), name='todo_lo_demas_api'),
]