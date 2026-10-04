from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Max
from .models import Cadastro
from .forms import CadastroForms

# Create your views here.
def resposta(request):

    return render (request, 'paginas/main.html')

def cadastro(request):
    
    if request.method == 'POST':
        
        formulario = CadastroForms(request.POST) 
        if formulario.is_valid():
            dados = formulario.cleaned_data

            #gerar matricula
            ultimo_id = Cadastro.objects.count()+1
            matricula = f'MATRICULA-{ultimo_id:02d}'

            #criar e salvar no banco
            alunos = Cadastro(
                nome_aluno = dados['nome_aluno'],
                data_nascimento = dados['data_nascimento'],
                nacionalidade_aluno = dados['nacionalidade_aluno'],
                nome_mae=dados['nome_mae'],
                numero_mae=dados['numero_mae'],
                nome_pai=dados['nome_pai'],
                numero_pai=dados['numero_pai'],
                endereco=dados['endereco'],
                bairro=dados['bairro'],
                numero_casa=dados['numero_casa'],
                telefone_extra=dados.get('telefone_extra'),
                turma=dados['turma'],
                matricula=matricula
            )
            alunos.save() #salvar no banco
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('cadastro')
        else:
            messages.error(request, 'Existem erros no formulário')
    else:
        
        formulario = CadastroForms()
    return render(request, 'paginas/cadastrar.html', {'formulario': formulario})