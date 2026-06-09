from dotenv import load_dotenv
from menus import menu_principal
from ui.tela_cadastro import tela_cadastro

load_dotenv()

if __name__ == "__main__":

    tela_cadastro()

    menu_principal()