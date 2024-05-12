from rest_framework import viewsets, status
from alimentos.api.serializers import CongelamentoSerializer
from alimentos.models import Congelamento
from django.shortcuts import get_object_or_404

from rest_framework.response import Response


class CongelamentoViewSet(viewsets.ModelViewSet):
    queryset = Congelamento.objects.all()
    serializer_class = CongelamentoSerializer

    def create(self, request):
        """
        Cria uma nova receita (congelamento).
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        """
        Obtém uma receita específica (congelamento) pelo ID.
        """
        congelamento = get_object_or_404(self.queryset, pk=pk)

        serializer = self.serializer_class(congelamento)
        return Response(serializer.data)

    def update(self, request, pk):
        """
        Atualiza uma receita (congelamento) existente.
        """
        congelamento = get_object_or_404(self.queryset, pk=pk)
        # Aqui, passe a instância de Congelamento
        serializer = self.serializer_class(congelamento, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk):
        """
        Exclui uma receita (congelamento) específica.
        """
        congelamento = get_object_or_404(self.queryset, pk=pk)
        congelamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
