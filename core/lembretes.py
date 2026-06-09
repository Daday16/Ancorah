from utils import horario_atual

historico = []


class Lembrete:

    def __init__(self, nome):
        self.nome = nome
        self.confirmado = False

    def notificar(self):

        while not self.confirmado:

            print(f"\n🔔 Lembrete: {self.nome}")
            print("1 - Tomado")
            print("2 - Adiar")

            escolha = input("Escolha: ")

            if escolha == "1":

                self.confirmado = True

                horario = horario_atual()

                historico.append(
                    f"{self.nome} confirmado às {horario}"
                )

                print("✅ Confirmado.")

            elif escolha == "2":
                print("⏰ Adiado por 5 segundos...")