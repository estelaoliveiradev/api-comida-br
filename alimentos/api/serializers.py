from rest_framework import serializers
from alimentos import models

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        fields = ('codigo', 'nome_categoria')

class AlimentoSerializer(serializers.ModelSerializer):
    nome_categoria_id = CategoriaSerializer(read_only=True, many=True)
    class Meta:
        model = models.Alimento
        fields = ('codigo', 'nome_alimento', 'nome_categoria', 'nome_categoria_id', 'kcal', 'porcao', 'data_cadastro', 'imagem')

class TipoPratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoPrato
        fields = ('codigo','nome_prato')

class CongelamentoSerializer(serializers.ModelSerializer):
    tipo_prato_id = TipoPratoSerializer(read_only=True)
    class Meta:
        model = models.Congelamento
        fields = ('codigo', 'nome_congelamento', 'descricao', 'modo_preparo','tempo_preparo', 'dificuldade', 'rendimento', 'imagem', 'tipo_prato_id')

class RefeicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Refeicao
        fields = ('codigo','nome_refeicao')

class CardapioSerializer(serializers.ModelSerializer):
    nome_refeicao_id = RefeicaoSerializer(read_only=True)
    congelamento_id = CongelamentoSerializer(read_only=True)
 
    class Meta:
        model = models.Cardapio
        fields = ('codigo','dia_semana', 'nome_refeicao', 'nome_refeicao_id', 'congelamento_id')