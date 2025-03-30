# aluno: João Pedro Cardoso de Liz

import json
import json.tool


def ler_arquivo_matriz():
    with open("matriz_controle_acesso.json", mode="r") as arquivo:
        # Lê o conteúdo do arquivo (arquivo.read()) e deserializa o
        # JSON para dicionário do Python (json.loads())
        return json.loads(arquivo.read())


def ler_arquivo_usuarios():
    with open("usuarios.json", "r") as arquivo:
        return json.loads(arquivo.read())


def listar_arquivos(login):
    usuario = buscar_usuario_matriz(login)
    if usuario is None:
        print("\nUsuário não encontrado ou sem permissões!")
        return

    arquivo_permitido = usuario['permissoes'].get('leitura')

    print("\nArquivos que você tem permissão para acessar:")
    for arquivo in arquivo_permitido:
        print(f"- {arquivo}")


def salvar_resultados(permissoes):
    # Abre arquivo para escrita para salvarmos o resultado das nossas operações
    with open('matriz_controle_acesso.json', mode='w') as arquivo:
        permissoes_serializado = json.dumps(permissoes)
        arquivo.write(permissoes_serializado)


def registrar_usuario():
    login = str(input("\nDigite o login: "))
    senha = str(input("Digite a senha: "))

    usuario = {
        'nome': login,
        'senha': senha
    }

    usuarios = ler_arquivo_usuarios()
    usuarios.append(usuario)

    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo)


def buscar_usuario(login):
    usuarios = ler_arquivo_usuarios()
    for usuario in usuarios:
        if usuario['nome'] == login:
            return usuarios.index(usuario)

    return None


def buscar_usuario_matriz(login):
    permissoes = ler_arquivo_matriz()
    for usuario in permissoes:
        if usuario['nome'] == login:
            return permissoes.index(usuario), usuario
    return None, None


def criar_arquivo(nome_arquivo, login, permissoes):
    index, usuario = buscar_usuario_matriz(login)

    if usuario is None:
        print("\nUsuário não encontrado na matriz de controle de acesso!")
        return

    permissoes[index]['permissoes'].setdefault('leitura').append(nome_arquivo)
    permissoes[index]['permissoes'].setdefault('escrita').append(nome_arquivo)
    permissoes[index]['permissoes'].setdefault('exclusao').append(nome_arquivo)

    salvar_resultados(permissoes)

    print(f"\nArquivo '{nome_arquivo}' adicionado às permissões do usuário '{login}'.")

def __init__():
    dados_json = ler_arquivo_usuarios()

    print("\n Seja bem-vindo ao controle de acesso! :D")

    anonimo = True
    while anonimo:
        print("""
        -_--_--_--_--_--_--_--_--_--_-
        [1] - Autenticação
        [2] - Cadastro
            
        [0] - Sair
        -_--_--_--_--_--_--_--_--_--_-
            """)
        opcao = int(input("===>>> "))

        if opcao == 1.0:
            login = str(input("Digite o login: "))
            senha = str(input("Digite a senha: "))

            busca = buscar_usuario(login)

            if busca is not None:
                login_cadastrado = dados_json[busca]['nome']
                senha_cadastrada = dados_json[busca]['senha']

                if login == login_cadastrado and senha == senha_cadastrada:
                    print(f"\nBem vindo {login}!")
                    anonimo = False

                    autenticado = True
                    while autenticado:
                        print("""
        -_--_--_--_--_--_--_--_--_--_-
        Opções de manipulação de arquivos:
            
        [1] - Listar
        [2] - Criar
        [3] - Excluir
        [4] - Leitura
        [5] - Escrita
            
        [0] - Sair
        -_--_--_--_--_--_--_--_--_--_-
                            """)

                        permissoes = ler_arquivo_matriz()

                        opcao = int(input("===>>> "))

                        if opcao == 1.0:
                            print("\nArquivos com permissão de leitura:")
                            listar_arquivos(login)

                        elif opcao == 2.0:
                            nome = str(input("Informe o nome do arquivo: "))
                            criar_arquivo(nome, login, permissoes)
                            print(
                                f"\nArquivo '{nome}' criado e adicionado às permissões do usuário '{login}'.")

                else:
                    print("\nSenha incorreta!")

            else:
                print("\nUsuário inexistente!")

        elif opcao == 2.0:
            registrar_usuario()
            print("\nUsuário cadastrado com sucesso!")

        elif opcao == 0.0:
            print("\nAté mais! :( \n")
            break

        else:
            print("\nOpção inválida! Tente novamente.")


__init__()
