from core.pomodoro import Pomodoro


def iniciar_pomodoro():

    print("\n====== POMODORO ======")

    minutos = int(
        input("Tempo de foco (10,15,25): ")
    )

    if minutos not in [10, 15, 25]:
        print("Tempo inválido.")
        return

    pomodoro = Pomodoro(minutos)

    pomodoro.iniciar()