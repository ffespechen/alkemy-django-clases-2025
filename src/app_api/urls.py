from django.urls import path 
from .views import (
    ArticuloListAPIView,
    ArticuloRetrieveAPIView
)

app_name = 'app_api'

urlpatterns = [
    path('', ArticuloListAPIView.as_view(), name='listar_api'),
    path('<int:pk>/', ArticuloRetrieveAPIView.as_view(), name='retrieve_api'),
]