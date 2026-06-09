import time


class Pomodoro:

    def __init__(self, minutos):
        self.minutos = minutos

    def iniciar(self):

        segundos = self.minutos * 60

        print("\n🧠 MODO FOCO ATIVADO")
        print("Menus ocultos...")
        print("-------------------")

        while segundos:

            mins = segundos // 60
            secs = segundos % 60

            tempo = f"{mins:02}:{secs:02}"

            print(f"\r⏳ {tempo}", end="")

            time.sleep(1)

            segundos -= 1

        print("\n\n🔔 Tempo finalizado!")
        print("🎵 Som suave...")