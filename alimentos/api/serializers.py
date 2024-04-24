from rest_framework import serializers
from alimentos import models


class AlimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alimento
        fields = ('codigo', 'nome_alimento', 'kcal', 'porcao', 'data_cadastro')

class CategoriaSerializer(serializers.ModelSerializer):
    nome_alimento = AlimentoSerializer(read_only=True, many=True)  # Nested serializer for related alimentos
    class Meta:
        model = models.Categoria
        fields = ('codigo', 'nome_categoria', 'nome_alimento')

class TipoPratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoPrato
        fields = ('codigo','nome_prato')

class CongelamentoSerializer(serializers.ModelSerializer):
    tipo_prato = TipoPratoSerializer(read_only=True)
    nome_alimento = AlimentoSerializer(many=True, read_only=True)
    class Meta:
        model = models.Congelamento
        fields = ('codigo', 'nome_congelamento', 'descricao', 'tempo_preparo', 'dificuldade', 'rendimento', 'imagem', 'tipo_prato', 'nome_alimento')

class RefeicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Refeicao
        fields = ('codigo','nome_refeicao')

class CardapioSerializer(serializers.ModelSerializer):
    nome_refeicao = RefeicaoSerializer(read_only=True)
    nome_alimento = AlimentoSerializer(read_only=True)
 
    class Meta:
        model = models.Cardapio
        fields = ('codigo','dia_semana', 'nome_refeicao', 'nome_alimento', 'nome_refeicao')