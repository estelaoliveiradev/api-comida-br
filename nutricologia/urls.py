from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from alimentos.api import AlimentoViewSet, CategoriaViewSet

urlpatterns = [
    path('api/', include('myapp.urls')),
]

urlpatterns += [
    path('api/alimentos/', AlimentoViewSet.as_urlpatterns()),
    path('api/categorias/', CategoriaViewSet.as_urlpatterns()),
]