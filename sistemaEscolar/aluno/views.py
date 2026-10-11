from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
from django.contrib import messages
from django.db.models import Max
from .models import Cadastro
from .forms import LoginForms, CadastroForms
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

       

        #verificaçao se é valido
        if form.is_valid():
            nome_login = form.cleaned_data['nome_login']
            senha= form.cleaned_data['senha']

            #senhas fixas
            NOME_LOGIN = 'Escola'
            SENHA = '1080'
           
            #verificaçao do user
            if nome_login == NOME_LOGIN and senha == SENHA:
                request.session['nome_login'] = nome_login
                messages.success(request, 'Logado com sucesso')
                return redirect('main')
            else:
                messages.error(request, 'Nome ou senha incorretos!')
                return redirect('login')
            
    return render(request, 'paginas/login.html', {'form': form})



def resposta(request):
    if 'nome_login' not in request.session:
        return redirect('login')
    return render (request, 'paginas/main.html')

def logout(request):
    request.session.flush()
    messages.info(request, 'Você saiu do programa')
    return redirect('login')


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

def pesquisar_alunos(request):
    #capturar o valor digitado no banco de dados
    nome_digitado = request.GET.get('nome_aluno')

    if nome_digitado:
        resultado_pesquisa = Cadastro.objects.filter(nome_aluno__icontains = nome_digitado)
    else:
        resultado_pesquisa = []

    return render(request, 'paginas/pesquisar.html' , {'aluno': resultado_pesquisa})

#mostrar ficha do aluno
def ficha_aluno(request, pk):
    #mostrar a ficha desse aluno completa do banco de dados no template pelo id
    
    ficha_estudante = get_object_or_404(Cadastro, pk = pk )
    return render(request, 'paginas/ficha_aluno.html', {'ficha_estudante': ficha_estudante})

def ficha_pdf(request, pk):
    estudante = get_object_or_404(Cadastro, pk=pk)
    converter_html = render_to_string('paginas/ficha_aluno.html', {'ficha_estudante': estudante})
    arquivo_pdf = HTML(string=converter_html, base_url=request.build_absolute_uri()).write_pdf()
    response = HttpResponse(arquivo_pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=ficha.pdf'
    return response
