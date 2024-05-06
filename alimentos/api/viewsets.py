from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from alimentos.api.serializers import CategoriaSerializer, TipoPratoSerializer
from alimentos.api.serializers import RefeicaoSerializer
from alimentos.models import Categoria, TipoPrato, Refeicao

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    def retrieve(self, request, pk):
        """
        Obtém uma categoria específica pelo ID.
        """
        categoria = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(categoria)
        return Response(serializer.data)

class TipoPratoViewSet(viewsets.ModelViewSet):
    queryset = TipoPrato.objects.all()
    serializer_class = TipoPratoSerializer
    def retrieve(self, request, pk):
        """
        Obtém um tipo de prato específico pelo ID.
        """
        tipo_prato = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(tipo_prato)
        return Response(serializer.data)


class RefeicaoViewSet(viewsets.ModelViewSet):
    queryset = Refeicao.objects.all()
    serializer_class = RefeicaoSerializer
    def retrieve(self, request, pk):
        """
        Obtém uma refeição específica pelo ID.
        """
        refeicao = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(refeicao)
        return Response(serializer.data)
        print(status.HTTP_200_OK)

