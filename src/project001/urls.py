"""
URL configuration for project001 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Router para API
from rest_framework import routers
from app_api.views import RelacionadoViewSet

router = routers.SimpleRouter()
router.register(r'relacionado', RelacionadoViewSet)


urlpatterns = [
    path('', include('app_auth.urls', namespace='app_auth')),
    path('api/', include('app_api.urls', namespace='app_api')),
    path('admin/', admin.site.urls),
    path('alkemy/', include('app_bienvenida.urls', namespace='app_bienvenida')),
    path('templates/', include('app_templates.urls', namespace='app_templates')),
    path('clases/', include('app_relacionada.urls', namespace='app_relacionada')),
]

urlpatterns += router.urls 
