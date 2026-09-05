import json
import random
from Json.arquivoJson import ArquivoJson

class Cadastro:
    def __init__(self, nome_aluno,data_nascimento,nome_mae, telefone_mae, nome_pai, 
                 telefone_pai, endereco,bairro,numero_casa, telefone_extra,turma, repositorio =None):
        self.nome_aluno = nome_aluno
        self.data_nascimento = data_nascimento
        self.nome_mae = nome_mae
        self.telefone_mae = telefone_mae
        self.nome_pai = nome_pai
        self.telefone_pai = telefone_pai
        self.endereco = endereco
        self.bairro = bairro
        self.numero_casa = numero_casa
        self.telefone_extra = telefone_extra
        self.turma = turma
        self.matricula = random.randint(1, 100)

       #criando instancia da classe json
        self.repositorio_json = repositorio or ArquivoJson()

    def registrar(self):

        aluno = {
                "Matricula": self.matricula,
                "Nome": self.nome_aluno, 
                "Data Nascimento": self.data_nascimento,
                "responsaveis": {
                    'Mãe':{
                        'Nome': self.nome_mae,
                        'Telefone mae': self.telefone_mae,
                    },
                    'Pai': {
                        'Nome': self.nome_pai,
                        'Telefone pai':self.telefone_pai
                    },
                    
    
                },
                "Endereco": self.endereco,
                "Bairro": self.bairro,
                "Numero Casa": self.numero_casa,
                "Telefone Extra": self.telefone_extra,
                "Turma": self.turma
            }

        #adicionar o aluno no json
        self.repositorio_json.adicionar(aluno)

        #salvar em arquivo json
        self.repositorio_json.salvar()
        print(f'Aluno cadastrado com sucesso!Nome do aluno : {self.nome_aluno} | Matrícula: {self.matricula}')

# classe criada para separar de registrar aluno, pois no cadastro pedia todos os parametros
class Gerenciador_Aluno:

    def __init__(self, repositorio = None):
        self.repositorio_json = repositorio or ArquivoJson()
    #@staticmethod #vai ser chamada diretamente pela classe
    def alterar(self):
        #pega o nome do aluno
        escolha = input('Digite o nome do aluno que deseja alterar informação:  ')
        
        for aluno in self.repositorio_json.lista_alunos: #percorre o aluno na lista de alunos
            if aluno['Nome'].strip().lower() == escolha.strip().lower(): # se o aluno que é um dicionario [dentro da chave nome] for igual a escolha
                print('Aluno(a) encontrado: ') #imprime aluno encontrado
                for chave, valor in aluno.items():#percorre chave e valor (valores do dicionario) retorna os pares do dicionario
                      print(f'{chave}: , {valor}')#imprima a chave e o valor

                #pergunta qual chave quer alterar
                informacao = input('Qual informação deseja alterar: (Digite o campo de informação igual:) ')
                if informacao in aluno and informacao != 'Matricula': #se a info está em aluno e informaçao é diferente de matricula
                        nova_info = input(f'Faça a alteração em {informacao} : ') #diz para fazer a alteraçao
                        aluno[informacao] = nova_info # o dicionario(aluno) na chave que foi perguntada recebe valor da alteração
                        self.repositorio_json.salvar() #salvar no json
                        print('Alterado com sucesso!')
                        alteracao_feita = input('Deseja ver os dados atualizados: Sim / Não: ').lower()
                        if alteracao_feita == 'sim':
                            print('DADOS ATUALIZADOS')
                            for chave, valor in aluno.items(): #aqui vai retornar os pares do dicionario atualizados
                                print(f'{chave} : {valor}')
                        else:
                            break
                else:
                  print("Campo inválido. Tente novamente.")
                break
        else:
            print("Aluno não encontrado.")

    def excluir_registro(self):
            
            excluir_aluno = input('Digite o nome do aluno que deseja excluir: ').strip().lower()
            alunos_sistema = [aluno for aluno in self.repositorio_json.lista_alunos if aluno['Nome'].strip().lower() == excluir_aluno]

            if not alunos_sistema:
                print('Aluno não encontrado!')
                return

            '''
            Verifica se tiver mais de um aluno com o mesmo nome, cria uma tupla(enumerate)
            com um indice e o nome do aluno
            '''
            if len(alunos_sistema) > 1:
                for indice, aluno in enumerate(alunos_sistema, start=1):
                    #mostra uma tupla com os nomes que tem na lista_alunos
                    print(f'{indice} - Matrícula: {aluno['Matricula']} | Nome: {aluno['Nome']}')

                #depois de listar pergunta qual vai apagar
                escolha = int(input('Digite o número do aluno a ser apagado: '))
                numero_escolhido = alunos_sistema[escolha - 1]
                self.repositorio_json.lista_alunos.remove(numero_escolhido)
            else:
                self.repositorio_json.lista_alunos.remove(alunos_sistema[0])


            with open(self.repositorio_json.arquivo,'w', encoding = 'utf-8') as arquivo:
                json.dump(self.repositorio_json.lista_alunos, arquivo, indent=2, ensure_ascii=False)

            print(f'Aluno {(excluir_aluno).title()} excluido com sucesso!')
    