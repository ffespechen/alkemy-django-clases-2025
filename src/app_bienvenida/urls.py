from django.urls import path
from . import views

app_name = 'app_bienvenida'

urlpatterns = [
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('saludar/<str:nombre>/', views.saludar, name='saludar'),
    path('cumpleanio/<int:anio>/<int:mes>/<int:dia>/', views.cumpleanio, name='cumpleanio'),
    path('html/', views.mensaje_html, name='mensaje_html'),
]
