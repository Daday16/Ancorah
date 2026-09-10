from dotenv import load_dotenv
from threading import Thread

from menus import menu_principal
from ui.tela_cadastro import tela_cadastro
from services.notificador import monitorar_lembretes

load_dotenv()

Thread(
    target=monitorar_lembretes,
    daemon=True
).start()

if __name__ == "__main__":

    tela_cadastro()

    menu_principal()