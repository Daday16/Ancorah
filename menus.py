from ui.tela_tarefas import menu_tarefas
from ui.tela_pomodoro import iniciar_pomodoro
from ui.tela_lembretes import menus_lembretes
from ui.tela_ia import iniciar_ia
from ui.tela_cadastro import tela_cadastro

def menu_principal():

    while True:

        print("\n====== TPAC ========")
        print("1 - Gerenciar Tarefas")
        print("2 - Pomodoro")
        print("3 - Lembretes")
        print("4 - Assistente IA")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":

            menu_tarefas()

        elif opcao == "2":

            iniciar_pomodoro()

        elif opcao == "3":

            menus_lembretes()

        elif opcao == "4":

            iniciar_ia()

        elif opcao == "0":

            print("Saindo...")
            break

        else:

            print("Opção inválida.")