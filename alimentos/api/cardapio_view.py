from rest_framework import viewsets, status
from alimentos.api.serializers import CardapioSerializer
from alimentos.models import Cardapio
from django.shortcuts import get_object_or_404

class CardapioViewSet(viewsets.ModelViewSet):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer

    def create(self, request):
        """
        Cria um novo cardápio.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        """
        Obtém um cardápio específico pelo ID.
        """
        cardapio = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(cardapio)
        return Response(serializer.data)

    def update(self, request, pk):
        """
        Atualiza um cardápio existente.
        """
        cardapio = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(cardapio, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk):
        """
        Exclui um cardápio específico.
        """
        cardapio = get_object_or_404(self.queryset, pk=pk)
        cardapio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)