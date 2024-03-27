from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from alimentos.api import viewsets as alimentoviewsets

route = routers.DefaultRouter()
route.register(r'alimentos', alimentoviewsets.AlimentoViewSet, basename="Alimentos")
route.register(r'categorias', alimentoviewsets.CategoriaViewSet, basename="Categorias")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]