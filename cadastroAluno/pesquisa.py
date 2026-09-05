import json
from Json.arquivoJson import ArquivoJson

class Pesquisa():
    def __init__(self):
         self.repositorio = ArquivoJson()

        

    def pesquisa_aluno(self):
        print("Lista carregada:", self.repositorio.lista_alunos)
        busca_aluno = input('Qual aluno procura: ')
        encontrado = False

        for aluno in self.repositorio.lista_alunos:
            if aluno['Nome'].strip().lower() == busca_aluno.strip().lower():
                print('Aluno encontrado!:\n')
                #aluno['Nome'] = aluno['Nome'].title()
                print(json.dumps(aluno, indent=2, ensure_ascii= False))
                encontrado = True
                break
        if not encontrado:
                print('Aluno não encontrado!')
                 