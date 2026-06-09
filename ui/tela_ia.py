from services.ia_service import IAService

ia = IAService()


def iniciar_ia():

    print("\n===== ASSISTENTE IA =====")

    while True:

        pergunta = input("\nVocê: ")

        if pergunta.lower() == "sair":
            print("Encerrando IA...")
            break

        resposta = ia.perguntar(pergunta)

        print(f"\nIA: {resposta}")