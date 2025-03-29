#aluno: João Pedro Cardoso de Liz

import json
import json.tool

def ler_arquivo_matriz():
    with open("matriz_controle_acesso.json", mode="r") as arquivo:
        # Lê o conteúdo do arquivo (arquivo.read()) e deserializa o
        # JSON para dicionário do Python (json.loads())
        permissoes = json.loads(arquivo.read())

    return permissoes
        
def ler_arquivo_usuarios():
    with open("usuarios.json", "r") as arquivo:
        dados_json = json.loads(arquivo.read())

    return dados_json

def editar_permissoes(permissoes):
    permissoes[0]['permissoes']

def remover_permissoes(permissoes, tipo, especifica):
    permissoes[0]['permissoes'][tipo].remove(especifica)

def salvar_resultados(permissoes):
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

    usuarios = ler_arquivo_usuarios()
    usuarios.append(usuario)

    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo)

def __init__():
    dados_json = ler_arquivo_usuarios()
    
    print ("\n Seja bem-vindo ao controle de acesso! :D")

    anonimo = True
    while anonimo:
        print("""
            -_--_--_--_--_--_--_--_--_--_-
            [1] - Autenticação
            [2] - Cadastro
            [3] - Sair
            -_--_--_--_--_--_--_--_--_--_-
            """)
        opcao = int(input("===>>> "))

        if opcao == 1.0:
            print("1234")

        elif opcao == 2.0:
            registrar_usuario()
            print("\nUsuário cadastrado com sucesso!")
            
    
__init__()