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
    index, usuario = buscar_usuario_matriz(login)

    if usuario is None:
        print("\nUsuário não encontrado ou sem permissões.")
        return

    arquivo_permitido = usuario['permissoes'].get('leitura')

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
        
        print("\nUsuário não encontrado na matriz de controle de acesso!")
    return None, None


def criar_arquivo(nome_arquivo, login, permissoes):
    index, usuario = buscar_usuario_matriz(login)

    #TO-DO
    #try catches para evitar exceção de arquivo não encontrado
    if usuario is not None:
        permissoes[index]['permissoes']['leitura'].append(nome_arquivo)
        permissoes[index]['permissoes']['escrita'].append(nome_arquivo)
        permissoes[index]['permissoes']['exclusao'].append(nome_arquivo)

    salvar_resultados(permissoes)

def excluir_arquivo(login, nome_arquivo, permissoes):
    index, usuario = buscar_usuario_matriz(login)
    #TO-DO
    #try catches para evitar exceção de arquivo não encontrado
    if usuario is not None and nome_arquivo in permissoes[index]['permissoes']['exclusao']:
        permissoes[index]['permissoes']['leitura'].remove(nome_arquivo)
        permissoes[index]['permissoes']['escrita'].remove(nome_arquivo)
        permissoes[index]['permissoes']['exclusao'].remove(nome_arquivo)

        print(f"\nArquivo '{nome_arquivo}' removido das permissões do usuário '{login}'.")

    else:
        print("\nAcesso negado.")

    salvar_resultados(permissoes)

def buscar_arquivo(nome_arquivo):
    permissoes = ler_arquivo_matriz()

    for usuario in permissoes:
        if nome_arquivo in usuario['permissoes'].get('leitura') or \
           nome_arquivo in usuario['permissoes'].get('escrita') or \
           nome_arquivo in usuario['permissoes'].get('exclusao'):
            return True  

    return False

def buscar_permissoes(permissao, usuario):
    return usuario['permissoes'].get(permissao)

def __init__():
    #TO-DO
    #identificar variaveis que podem ser declaradas ao inicio do codigo.
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
            login = str(input("\nDigite o login: "))
            senha = str(input("Digite a senha: "))

            busca = buscar_usuario(login)

            if busca is not None:
                login_cadastrado = dados_json[busca]['nome']
                senha_cadastrada = dados_json[busca]['senha']

                if login == login_cadastrado and senha == senha_cadastrada:
                    print(f"\nBem vindo(a) {login}!")
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
            
        [0] - Voltar
        -_--_--_--_--_--_--_--_--_--_-
                            """)

                        permissoes = ler_arquivo_matriz()

                        opcao = int(input("===>>> "))

                        if opcao == 1:
                            print("\nArquivos com permissão de leitura:")
                            listar_arquivos(login)

                        elif opcao == 2:
                            nome = str(input("\nInforme o nome do arquivo: "))

                            if buscar_arquivo(nome):
                                print(f"\nO arquivo '{nome}' já existe!")
        
                            else:
                                criar_arquivo(nome, login, permissoes)
                                print(
                                    f"\nArquivo '{nome}' criado e adicionado às permissões do usuário '{login}'.")
                            
                        elif opcao == 3:
                            nome = str(input("\nInforme o nome do arquivo: "))
                            excluir_arquivo(login, nome, permissoes)

                        elif opcao == 4:
                            index, usuario = buscar_usuario_matriz(login)
                            arquivos = buscar_permissoes("leitura", usuario)

                            print("\n Selecione o arquivo desejado: \n")
                            for arquivo in arquivos:
                                print(f"[{arquivos.index(arquivo) + 1}] - {arquivo}")

                            print("\n[0] - Voltar")

                            leitura = int(input("\n===>>> "))

                            if 1 <= leitura <= len(arquivos):
                                print("""
        Lendo o arquivo...
                                  
        ==>>
                                ,..........   ..........,         
                            ,..,'          '.'          ',..,     
                            ,' ,'            :            ', ',    
                            ,' ,'             :             ', ',   
                            ,' ,'              :              ', ',  
                            ,' ,'............., : ,.............', ', 
                            ,'  '............   '.'   ............'  ',
                            '''''''''''''''''';''';'''''''''''''''''' 
                                                '''            
                                              
                                        """)
                                
                            elif leitura == 0:
                                print("\nVoltando...")
                                
                            else:
                                print("\nOpção inválida.")

                        elif opcao == 5:
                            index, usuario = buscar_usuario_matriz(login)

                            escrita_permitida = buscar_permissoes("escrita", usuario)
                            arquivos = buscar_permissoes("leitura", usuario)

                            print("\n Selecione o arquivo desejado: \n")
                            for arquivo in arquivos:
                                print(f"[{arquivos.index(arquivo) + 1}] - {arquivo}")
                                if arquivo in escrita_permitida:
                                    permitido = arquivo

                            print("\n[0] - Voltar")

                            leitura = int(input("\n===>>> "))

                            if 1 <= leitura <= len(arquivos):
                                if arquivos.index(permitido) + 1 == leitura:
                                    print("\nAcesso liberado.")
                                    escrita = str(input("\nDigite suas alterações desejadas: "))
                                    print("\nArquivo alterado.")

                                else:
                                    print("\nAcesso negado.")

                            elif leitura == 0:
                                print("\nVoltando...")

                        elif opcao == 0:
                            print("\nVoltando à tela de autenticação e cadastro...")
                            autenticado = False
                            anonimo = True

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