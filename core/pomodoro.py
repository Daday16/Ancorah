import time
import msvcrt

class Pomodoro:

    def __init__(self, minutos):
        self.minutos = minutos

    def iniciar(self):

        segundos = self.minutos * 60

        print("\n🧠 MODO FOCO ATIVADO")
        print("Menus ocultos...")
        print("-------------------")
        print("Pressione Q para cancelar.\n")

        while segundos > 0:

            if msvcrt.kbhit():

                tecla = msvcrt.getch().decode(
                    "utf-8",
                    errors="ignore"
                ).lower()

                if tecla == "q":

                    print("\n\n❌ Pomodoro cancelado.")
                    return

            mins = segundos // 60
            secs = segundos % 60

            print(f"\r⏳ {mins:02}:{secs:02}", end="")

            time.sleep(1)

            segundos -= 1

        print("\n\n✅ Tempo finalizado!")