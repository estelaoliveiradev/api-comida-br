from rest_framework import viewsets
from alimentos.api.serializers import AlimentoSerializer, CategoriaSerializer, TipoPratoSerializer
from alimentos.api.serializers import ReceitaSerializer, RefeicaoSerializer, CardapioSerializer
from alimentos.models import Alimento, Categoria, TipoPrato, Receita, Refeicao, Cardapio


class AlimentoViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class TipoPratoViewSet(viewsets.ModelViewSet):
    queryset = TipoPrato.objects.all()
    serializer_class = TipoPratoSerializer

class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

class RefeicaoViewSet(viewsets.ModelViewSet):
    queryset = Refeicao.objects.all()
    serializer_class = RefeicaoSerializer

class CardapioViewSet(viewsets.ModelViewSet):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer