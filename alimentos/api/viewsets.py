from rest_framework import viewsets
from alimentos.api.serializers import AlimentoSerializer, CategoriaSerializer
from alimentos.models import Alimento, Categoria


class AlimentoViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer