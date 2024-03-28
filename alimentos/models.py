from django.db import models
from uuid import uuid4

# Tabela Categoria - descricao categoria do alimento
class Categoria(models.Model):
    id_categoria = models.UUIDField(primary_key=True, default=uuid4, editable=True)
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
 
 # Tabela Alimento - seria cada igrediente da receita   
class Alimento(models.Model):
    id_alimento = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    kcal = models.IntegerField()
    porcao = models.CharField(max_length=255)
    data_cadastro = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to="alimentos/", blank=True, null=True)

    def __str__(self):
        return self.nome  
# Tabela tipo de prato - definição se é acompanhamento, prato principal ou salada
class TipoPrato(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

# Tabela Receita - Onde o usuário irá consultar receitas
class Receita(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    tempo_preparo = models.IntegerField()
    dificuldade = models.CharField(max_length=1)
    rendimento = models.IntegerField()
    imagem = models.ImageField(upload_to="receitas/", blank=True, null=True)
    tipo_prato = models.ForeignKey(TipoPrato, on_delete=models.CASCADE)

    # Relacionamento muitos para muitos com a tabela Alimentos
    alimentos = models.ManyToManyField(Alimento)

    def __str__(self):
        return self.nome
    
# Tabela Refeicao - descreve se for Almoço ou Jantar
class Refeicao(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

# Tabela Cardapio - Traz o cardápio para o usuário   
class Cardapio(models.Model):
    dia = models.CharField(max_length=1)
    refeicao = models.ForeignKey(Refeicao, on_delete=models.CASCADE)
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.dia} - {self.refeicao.nome} - {self.alimento.nome}"
    

    
