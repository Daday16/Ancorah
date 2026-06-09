from core.tarefas import (
    criar_tarefa,
    listar_tarefas,
    concluir_tarefa,
    adicionar_subtarefa,
    listar_subtarefas,
    excluir_tarefa
)


def menu_tarefas():

    while True:

        print("\n====== TAREFAS ======")
        print("1 - Criar tarefa")
        print("2 - Listar tarefas")
        print("3 - Adicionar subtarefa")
        print("4 - Concluir tarefa")
        print("5 - Excluir tarefa")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":

            titulo = input("Título da tarefa: ")
            criar_tarefa(titulo)

        elif opcao == "2":

            listar_tarefas()

        elif opcao == "3":

            listar_tarefas()

            indice = int(
                input("Número da tarefa: ")
            )

            titulo = input(
                "Título da subtarefa: "
            )

            adicionar_subtarefa(
                indice,
                titulo
            )

            listar_subtarefas(
                indice
            )

        elif opcao == "4":

            listar_tarefas()

            indice = int(
                input("Número da tarefa concluída: ")
            )

            concluir_tarefa(indice)

        elif opcao == "5":

            listar_tarefas()

            indice = int(
                input("Número da tarefa a excluir: ")
            )

            confirmar = input(
                "Tem certeza? (s/n): "
            ).lower()

            if confirmar == "s":
                excluir_tarefa(indice)

        elif opcao == "0":

            break

        else:

            print("Opção inválida.")