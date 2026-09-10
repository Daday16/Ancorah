from core.usuarios import cadastrar_usuario


def tela_cadastro():

    print("\n===== CADASTRO =====")

    nome = input("Nome: ")
    email = input("E-mail: ")

    cadastrar_usuario(nome, email)

    