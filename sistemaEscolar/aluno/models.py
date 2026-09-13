from django.db import models

# Create your models here.

class Cadastro(models.Model):
    #representar no banco
    nome_aluno = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    nacionalidade_aluno = models.CharField(max_length= 30)
    nome_mae = models.CharField(max_length= 200, blank= True)
    numero_mae = models.CharField(max_length=20, blank=True)
    nome_pai = models.CharField(max_length=200, blank= True)
    numero_pai = models.CharField(max_length=20, blank= True)
    endereco = models.CharField(max_length= 200)
    bairro = models.CharField(max_length=100)
    numero_casa = models.CharField(max_length=20)
    telefone_extra = models.CharField(max_length=20, blank= True, null=True)
    turma = models.CharField(max_length=50)
    matricula = models.PositiveIntegerField(unique=True)

def __str__(self):
    return f'{self.nome_aluno} - Matrícula - {self.matricula} realizada com sucesso!'
