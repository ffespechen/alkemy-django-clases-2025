from django.urls import path
from . import views

app_name='app_templates'

urlpatterns = [
    path('primero/', views.primer_template, name='primero'),
    path('bootstrap/', views.bootstap_template, name='bootstrap'),
    path('heredero1/<str:titulo>/<str:contenido>/', views.vista_heredero1, name='heredero1'),
    path('listar/', views.listar_articulos, name='listar'),
    path('listar_json/', views.listar_json, name='listar_json',),
    path('detalle/<int:id>/', views.detalle_articulo, name='detalle'),
    path('borrar/<int:id>/', views.borrar_articulo, name='borrar'),
    path('modificar_promocion/<int:id>/', views.modificar_promocion, name='modificar_promocion'),
    path('crear/', views.ArticuloCreateView.as_view(), name='crear'),
    path('modificar/<int:pk>/', views.ArticuloUpdateView.as_view(), name='modificar'),
]