from rest_framework import serializers  # type: ignore
from alimentos import models


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        fields = ('nome_categoria',)


class AlimentoSerializer(serializers.ModelSerializer):
    nome_categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Categoria.objects.all())

    class Meta:
        model = models.Alimento
        fields = '__all__'


class TipoPratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoPrato
        fields = '__all__'


class CongelamentoSerializer(serializers.ModelSerializer):
    # Access the nested serializer
    tipo_prato = TipoPratoSerializer(read_only=True)

    class Meta:
        model = models.Congelamento
        fields = ('codigo', 'nome_congelamento', 'descricao', 'modo_preparo',
                  'tempo_preparo', 'dificuldade', 'rendimento', 'imagem', 'tipo_prato')


class RefeicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Refeicao
        fields = '__all__'


class CardapioSerializer(serializers.ModelSerializer):
    nome_refeicao_id = RefeicaoSerializer()
    nome_alimento = CongelamentoSerializer()
    nome_categoria = CategoriaSerializer()

    class Meta:
        model = models.Cardapio
        fields = '__all__'


# class AlmocoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Cardapio  # Supondo que 'Refeicao' seja o modelo
#         fields = '__all__'  # Ou especifique os campos desejados

# class JantarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Cardapio  # Supondo que 'Refeicao' seja o modelo
#         fields = '__all__'  # Ou especifique os campos desejados
