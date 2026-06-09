import json
import os

ARQUIVO = 'data/chat_history.json'

class MemoriaService:

    @staticmethod
    def carregar():

        if not os.path.exists(ARQUIVO):
            return []

        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def salvar(historico):

        with open(ARQUIVO, 'w', encoding='utf-8') as f:
            json.dump(historico, f, indent=4, ensure_ascii=False)