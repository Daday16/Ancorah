from core.lembretes import Lembrete, historico


def menus_lembretes():

    while True:

        print("\n====== LEMBRETES ======")
        print("1 - Novo lembrete")
        print("2 - Ver histórico")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":

            nome = input("Nome do lembrete: ")

            lembrete = Lembrete(nome)
            lembrete.notificar()

        elif opcao == "2":

            print("\n📜 Histórico")

            for h in historico:
                print(h)

        elif opcao == "0":
            break