#alunos: João Pedro Cardoso de Liz

import json
import json.tool

def ler_arquivo_matriz():
    with open("matriz_controle_acesso.json", mode="r") as arquivo:
        # Lê o conteúdo do arquivo (arquivo.read()) e deserializa o
        # JSON para dicionário do Python (json.loads())
        permissoes = json.loads(arquivo.read())
        
def ler_arquivo_usuarios():
    with open("usuarios.json", "r") as arquivo:
        dados_json = json.loads(arquivo.read())
        return dados_json

def editar_permissoes():
    permissoes[0]['permissoes']

def remover_permissoes():
    permissoes[0]['permissoes']['leitura'].remove('notas.csv')

def salvar_resultados():
    # Abre arquivo para escrita para salvarmos o resultado das nossas operações
    with open('matriz_controle_acesso.json', mode='w') as arquivo:
        # Serializa a variável permissões para JSON
        permissoes_serializado = json.dumps(permissoes)

        # Salvar no arquivo especificado
        arquivo.write(permissoes_serializado)
        
def registrar_usuario():
    login = str(input("Digite o login: "))
    senha = str(input("Digite a senha: "))
    usuario = {
        'nome': login,
        'senha': senha
    }
    
    with open("usuarios.json", "w") as arquivo:
        json.dump(usuario, arquivo)
    
    return login, senha

def __init__():
        
    # TO-DO
    # criar uma variavel 'dados_json' para chamar a função de leitura
    
    login_cadastrado = dados_json['nome']
    senha_cadastrada = dados_json['senha']
    
    