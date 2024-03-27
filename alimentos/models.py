from django.db import models
from uuid import uuid4


class Alimento(models.Model):
    id_alimento = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    kcal = models.IntegerField()
    porcao = models.CharField(max_length=255)
    data_cadastro = models.DateField(auto_now_add=True)
   
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE, related_name='categorias')  # Specify related_name
