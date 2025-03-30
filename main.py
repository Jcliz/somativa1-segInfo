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
    permissoes = ler_arquivo_matriz()

    for usuario in permissoes:
        if usuario['nome'] == login:
            print("\nArquivos com permissão de leitura:")

            # Combina todas as permissões em uma única lista     
            arquivo_leitura = usuario['permissoes'].get('leitura')   

            # Lista os arquivos únicos
            for arquivo in arquivo_leitura:
                print(f"- {arquivo}")
            return

    print("\nUsuário não encontrado ou sem permissões!")


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
                            listar_arquivos(login)

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
