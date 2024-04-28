from django.db import models
from uuid import uuid4

# Tabela Categoria - descricao categoria do alimento
class Categoria(models.Model):
    codigo = models.IntegerField(primary_key=True, editable=True)
    nome_categoria = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
 
 # Tabela Alimento - seria cada igrediente da receita   
class Alimento(models.Model):
    codigo = models.IntegerField(primary_key=True, editable=False)
    nome_alimento = models.CharField(max_length=255)
    nome_categoria = models.CharField(max_length=255)
    # relacionamento um para muitos
    nome_categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    kcal = models.IntegerField()
    porcao = models.CharField(max_length=255)
    data_cadastro = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to="alimentos/", blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.nome_alimento} - {self.nome_categoria} -{self.porcao}"  
# Tabela tipo de prato - definição se é acompanhamento, prato principal ou salada
class TipoPrato(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome_prato = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_prato

# Tabela Receita - Onde o usuário irá consultar receitas
class Congelamento(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome_congelamento = models.CharField(max_length=255)
    descricao = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    dificuldade = models.CharField(max_length=1)
    rendimento = models.IntegerField()
    imagem = models.ImageField(upload_to="receitas/", blank=True, null=True)
    tipo_prato_id = models.ForeignKey(TipoPrato, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.nome_congelamento} - {self.descricao} - {self.modo_preparo} - {self.tempo_preparo} - {self.dificuldade} - {self.tipo_prato_id}"
    
# Tabela Refeicao - descreve se for Almoço ou Jantar
class Refeicao(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome_refeicao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_refeicao

# Tabela Cardapio - Traz o cardápio para o usuário   
class Cardapio(models.Model):
    codigo = models.IntegerField(primary_key=True)
    dia_semana = models.CharField(max_length=1)
    nome_refeicao_id = models.ForeignKey(Refeicao, on_delete=models.CASCADE)
    congelamento_id = models.ForeignKey(Congelamento, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.dia} - {self.nome_refeicao_id.nome} "
    

    
