from rest_framework import serializers
from alimentos import models

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        fields = '__all__'

class AlimentoSerializer(serializers.ModelSerializer):
    nome_categoria_id = CategoriaSerializer(read_only=True, many=True)
    class Meta:
        model = models.Alimento
        fields = '__all__'

class TipoPratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoPrato
        fields = '__all__'

class CongelamentoSerializer(serializers.ModelSerializer):
    tipo_prato_id = TipoPratoSerializer(read_only=True)
    class Meta:
        model = models.Congelamento
        fields = '__all__'

class RefeicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Refeicao
        fields = '__all__'

class CardapioSerializer(serializers.ModelSerializer):
    nome_refeicao_id = RefeicaoSerializer(read_only=True)
    congelamento_id = CongelamentoSerializer(read_only=True)
 
    class Meta:
        model = models.Cardapio
        fields = '__all__'