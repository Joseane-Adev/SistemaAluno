#criando um cadastro de alunos
from cadastroAluno.cadastro import Cadastro
from cadastroAluno.pesquisa import Pesquisa
from cadastroAluno.validaçoes import Validacao
from Json.arquivoJson import ArquivoJson
from cadastroAluno.cadastro import Gerenciador_Aluno


class Visual(): 

    def __init__(self):
        self.repositorio_json = ArquivoJson()

    def mostrar_menu(self):
        while True: 
            print('*' * 40)
            print('SISTEMA DE CADASTRO ESCOLA SONHO ENCANTADO')
            print('1 - Cadastrar')
            print('2- Pesquisar aluno(a)')
            print('3- Alterar informações')
            print('4- Excluir aluno(a)')
            print('5 - Sair')
            escolha = int(input('Escolha uma das opçoes: '))

            if escolha == 1:
                self.cadastrar_aluno()
            elif escolha == 2:
                pesquisa = Pesquisa() #criando o objeto
                pesquisa.pesquisa_aluno() #chamando o objeto
                '''
                para alterar e excluir so está passando o repositorio
                '''
            elif escolha == 3:
                gerenciador = Gerenciador_Aluno(repositorio= self.repositorio_json)
                gerenciador.alterar()
            elif escolha == 4:
                gerenciador = Gerenciador_Aluno(repositorio= self.repositorio_json)
                gerenciador.excluir_registro()
            elif escolha == 5:
                print('Encerrando programa')
                break
            else:
                print('Opcão inválida') 
    
    def cadastrar_aluno(self):
        while True: 
            nome_aluno = Validacao.valida_nomes('Digite o nome do aluno(a): ').title()
            data_nascimento = input("Digite a data de nascimento: ")

            #dados da mae
            nome_mae = Validacao.valida_nomes('Digite o nome da mãe: ').title()
            telefone_mae = Validacao.valida_telefones('Digite o numero da mãe (9 digitos): ')
                
            #dados do pai
            nome_pai = Validacao.valida_nomes('Digite o nome do pai: ').title()
            telefone_pai = Validacao.valida_telefones('Digite o numero da pai (9 digitos): ')
    

            endereco = input("Digite o endereço: ").title()
            bairro = input('Digite o bairro: ').title()
            numero_casa = int(input('Número da casa: ')) 
            #telefone extra
            while True: 
                telefone_extra = input('Deseja cadastrar um telefone extra: ( Sim ou Não)').title()
                if telefone_extra == 'Sim':
                    telefone = input("Digite o telefone: (9 digitos) ")
                    if len(telefone) == 9 and telefone.isdigit():
                        break
                    else:
                        print('Telefone inválido, Digite somente 9 numeros')
                else:
                    print('Telefone extra não cadastrado!')
                    break

            turma = input("Digite a turma: ")

            aluno = Cadastro(nome_aluno, data_nascimento,nome_mae,telefone_mae,nome_pai,telefone_pai, endereco, bairro, numero_casa, telefone_extra , turma)
            aluno.registrar()
        
    
            continuar = input('Deseja cadastrar outro aluno(a): Sim ou Não: ').lower()
            if continuar == 'sim':
                continue
            elif continuar == 'nao':
                print('Saindo do cadastro')
                break
            else:
                print('Opcão inválida') 


        
    
        




