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

class TipoPratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoPrato
        fields = ('nome')

class ReceitaSerializer(serializers.ModelSerializer):
    tipo_prato = TipoPratoSerializer(read_only=True)
    alimentos = AlimentoSerializer(many=True, read_only=True)
    class Meta:
        model = models.Receita
        fields = ('id_receita', 'nome', 'descricao', 'tempo_preparo', 'dificuldade', 'rendimento', 'imagem', 'tipo_prato', 'alimentos')

class RefeicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Refeicao
        fields = ('nome')

class CardapioSerializer(serializers.ModelSerializer):
    refeicao = RefeicaoSerializer(read_only=True)
    alimento = AlimentoSerializer(read_only=True)
    class Meta:
        model = models.Cardapio
        fields = ('dia', 'refeicao', 'alimento')