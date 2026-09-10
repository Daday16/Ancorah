from core.lembretes import (
    criar_lembrete,
    listar_lembretes,
    listar_pendentes,
    concluir_pendente,
    adiar_pendente
)


def menus_lembretes():

    while True:

        print("\n====== LEMBRETES ======")
        print("1 - Novo lembrete")
        print("2 - Ver lembretes")
        print("3 - Lembretes pendentes")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":

            titulo = input("Título: ")
            data = input("Data (dd/mm/aaaa): ")
            hora = input("Hora (hh:mm): ")

            criar_lembrete(titulo, data, hora)

        elif opcao == "2":

            listar_lembretes()

        elif opcao == "3":

            pendentes = listar_pendentes()

            if not pendentes:
                print("\n✅ Nenhum lembrete pendente.")
                continue

            print("\n===== LEMBRETES PENDENTES =====\n")

            for lembrete in pendentes:

                data = lembrete[2].strftime("%d/%m/%Y")
                hora = str(lembrete[3])[:5]

                print(f"ID: {lembrete[0]}")
                print(f"Título: {lembrete[1]}")
                print(f"📅 {data}")
                print(f"🕒 {hora}")
                print("-" * 30)

            try:

                id_lembrete = int(
                    input("\nDigite o ID do lembrete (0 para voltar): ")
                )

                if id_lembrete == 0:
                    continue

                print("\n1 - Marcar como concluído")
                print("2 - Adiar 5 minutos")
                print("3 - Adiar 15 minutos")
                print("4 - Adiar 30 minutos")
                print("0 - Cancelar")

                escolha = input("Escolha: ")

                if escolha == "1":

                    concluir_pendente(id_lembrete)

                    print("\n✅ Lembrete concluído!")

                elif escolha == "2":

                    adiar_pendente(id_lembrete, 5)

                    print("\n⏰ Lembrete adiado por 5 minutos.")

                elif escolha == "3":

                    adiar_pendente(id_lembrete, 15)

                    print("\n⏰ Lembrete adiado por 15 minutos.")

                elif escolha == "4":

                    adiar_pendente(id_lembrete, 30)

                    print("\n⏰ Lembrete adiado por 30 minutos.")

                elif escolha == "0":

                    continue

                else:

                    print("\n❌ Opção inválida.")

            except ValueError:

                print("\n❌ Digite um número válido.")

        elif opcao == "0":

            break

        else:

            print("\n❌ Opção inválida.")