from rest_framework import serializers
from alimentos import models


class AlimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alimento
        fields = ('id_alimento', 'nome', 'kcal', 'porcao', 'data_cadastro')

class CategoriaSerializer(serializers.ModelSerializer):
    alimentos = AlimentoSerializer(read_only=True, many=True)  # Nested serializer for related alimentos

    class Meta:
        model = models.Categoria
        fields = ('id_categoria', 'nome', 'alimentos')