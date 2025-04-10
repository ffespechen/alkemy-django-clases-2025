from django.urls import path
from .views import (
    RelacionadoListView,
    RelacionadoCreateView,
    RelacionadoUpdateView,
    RelacionadoDeleteView,
    relacionado_detalle
)

app_name = 'app_relacionada'

urlpatterns = [
    path('', RelacionadoListView.as_view(), name='listar'),
    path('crear/', RelacionadoCreateView.as_view(), name='crear'),
    path('modificar/<int:pk>/', RelacionadoUpdateView.as_view(), name='modificar'),
    path('borrar/<int:pk>/', RelacionadoDeleteView.as_view(), name='borrar'),
    path('detalle/<int:pk>/', relacionado_detalle, name='detale')
]