from rest_framework import viewsets
from alimentos.api.serializers import AlimentoSerializer, CategoriaSerializer, TipoPratoSerializer
from alimentos.api.serializers import CongelamentoSerializer, RefeicaoSerializer, CardapioSerializer
from alimentos.models import Alimento, Categoria, TipoPrato, Congelamento, Refeicao, Cardapio


class AlimentoViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class TipoPratoViewSet(viewsets.ModelViewSet):
    queryset = TipoPrato.objects.all()
    serializer_class = TipoPratoSerializer

class CongelamentoViewSet(viewsets.ModelViewSet):
    queryset = Congelamento.objects.all()
    serializer_class = CongelamentoSerializer

class RefeicaoViewSet(viewsets.ModelViewSet):
    queryset = Refeicao.objects.all()
    serializer_class = RefeicaoSerializer

class CardapioViewSet(viewsets.ModelViewSet):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer