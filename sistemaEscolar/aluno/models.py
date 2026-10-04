from django.db import models

# Create your models here.

class Cadastro(models.Model):
    #representar no banco
    nome_aluno = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    nacionalidade_aluno = models.CharField(max_length= 30)
    nome_mae = models.CharField(max_length= 100, blank= True)
    numero_mae = models.CharField(max_length=20, blank=True)
    nome_pai = models.CharField(max_length=100, blank= True)
    numero_pai = models.CharField(max_length=20, blank= True)
    endereco = models.CharField(max_length= 100)
    bairro = models.CharField(max_length=100)
    numero_casa = models.CharField(max_length=20)
    telefone_extra = models.CharField(max_length=20, default='', blank=True)
    turma = models.CharField(max_length=50)
    matricula = models.CharField(max_length=20, blank=True)
    

