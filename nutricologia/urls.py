from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from alimentos.api import viewsets as alimentoviewsets
from alimentos.api import alimento_view, cardapio_view, congelamento_view

route = routers.DefaultRouter()
route.register(r'alimentos', alimento_view.AlimentoViewSet, basename="Alimentos")
route.register(r'categorias', alimentoviewsets.CategoriaViewSet, basename="Categorias")
route.register(r'tipoprato', alimentoviewsets.TipoPratoViewSet, basename="TipoPrato")
route.register(r'cardapio', cardapio_view.CardapioViewSet, basename="Cardapio")
route.register(r'refeicao', alimentoviewsets.RefeicaoViewSet, basename="Refeicao")
route.register(r'congelamento', congelamento_view.CongelamentoViewSet, basename="Congelamento")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]