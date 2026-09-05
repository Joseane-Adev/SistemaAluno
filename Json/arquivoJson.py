import os
import json

'''
os.path.exists
Verifica se o arquivo alunos.json já existe no diretório.Se não existir, significa que ainda não há dados salvos.
with open('alunos.json', 'r', encoding='utf-8') as alunos: Abre o arquivo em modo leitura ('r') com codificação UTF-8.
O with garante que o arquivo será fechado automaticamente depois.

json.load(alunos)
Lê o conteúdo do arquivo e transforma em uma lista ou dicionário Python.
Exemplo: se o arquivo tiver [{"Nome":"Carlos"}], vira uma lista com um dicionário dentro.

except json.JSONDecodeError:
Se o arquivo estiver vazio ou corrompido, o json.load dá erro.
Nesse caso, o código cria uma lista vazia (lista_alunos = []) para evitar que o programa quebre.
'''
class ArquivoJson:
    
    def __init__(self, arquivo = 'alunos.json'):
        self.arquivo = arquivo
        self.lista_alunos = self.carregar()

    def carregar(self): 
        if os.path.exists(self.arquivo):
            with open(self.arquivo ,'r', encoding='utf-8') as alunos:
                try:
                    return json.load(alunos)
                except json.JSONDecodeError:
                    return [] #lista vazia se estiver corrompido o json
        else:
            return [] # lista vazia se o arquio não existir

    def salvar(self):
            # salvar no arquivo JSON
        with open(self.arquivo, 'w', encoding='utf-8') as salve:
                json.dump(self.lista_alunos, salve, indent=2, ensure_ascii=False)

    def adicionar(self, aluno):
        self.lista_alunos.append(aluno)
        self.salvar()