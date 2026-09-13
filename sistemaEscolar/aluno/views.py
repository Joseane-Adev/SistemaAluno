from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Max
from .models import Cadastro

# Create your views here.
def resposta(request):

    return render (request, 'paginas/main.html')

def cadastro(request):
    
    if request.method == 'POST':
        ultima_matricula = Cadastro.objects.aggregate(Max('matricula'))['matricula__max'] or 0
        nova_matricula = ultima_matricula + 1
        Cadastro.objects.create(
            nome_aluno = request.POST.get('nome_aluno'),
            data_nascimento=request.POST.get('data_nascimento'),
            nacionalidade_aluno=request.POST.get('nacionalidade_aluno'),
            nome_mae=request.POST.get('nome_mae'),
            numero_mae=request.POST.get('numero_mae'),
            nome_pai=request.POST.get('nome_pai'),
            numero_pai=request.POST.get('numero_pai'),
            endereco=request.POST.get('endereco'),
            bairro=request.POST.get('bairro'),
            numero_casa=request.POST.get('numero_casa'),
            telefone_extra=request.POST.get('telefone_extra'),  # cuidado com o nome do campo
            turma=request.POST.get('turma'),
            matricula= nova_matricula,
        )
        messages.success(request, f'Aluno(a):matriculado com sucesso! Matrícula: {nova_matricula}')#mensagem de aviso
    
    return render (request, 'paginas/cadastrar.html')