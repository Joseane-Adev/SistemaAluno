import re
'''
A validaçao recebe nomes, fiz para usar com nome_alun0(a), nome_pai e nome_mae
importei um regex. Essa regex só aceita strings compostas por letras (com ou sem acento) e espaços.

'''
class Validacao:

# validação nome aluno
    def valida_nomes(nomes):
        while True: 
            nome = input(nomes)
            if re.match((r'^[A-Za-zÀ-ÿ\s]+$'), nome):
                return nome
            else:
                print('Nome inválido! Digite apenas letras e espaços')

    def valida_telefones(numero_telefone):
        while True:
            telefones = input(numero_telefone)
            if (telefones.isdigit() and len(telefones) == 9):
                return telefones #retorna o telefone válido
            else:
                print('Telefone inválido! Digite apenas 9 números')