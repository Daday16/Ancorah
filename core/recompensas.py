pontos_usuario = 0


def adicionar_pontos(pontos):
    global pontos_usuario
    pontos_usuario += pontos
    print(f"\n✨ +{pontos} pontos!")
    print(f"🏆 Total: {pontos_usuario}")