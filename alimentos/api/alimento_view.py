from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from alimentos.models import Alimento
from .serializers import AlimentoSerializer

class AlimentoViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer

    def create(self, request):
        """
        Cria um novo alimento.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        """
        Obtém um alimento específico pelo ID.
        """
        alimento = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(alimento)
        return Response(serializer.data)

    def update(self, request, pk):
        """
        Atualiza um alimento existente.
        """
        alimento = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(alimento, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk):
        """
        Exclui um alimento específico.
        """
        alimento = get_object_or_404(self.queryset, pk=pk)
        alimento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)