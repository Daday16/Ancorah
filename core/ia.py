import requests


class AssistenteIA:

    def conversar(self, mensagem):

        prompt = f"""
Você é uma organizadora, guia gentil, cérebro auxiliar e destravadora de tarefas.

REGRAS:
- Responda em português.
- Seja objetiva.
- Máximo 3 frases.
- Dê ações práticas.
- Não faça discursos motivacionais.
- Não peça mais informações sem necessidade.

Usuária:
{mensagem}

Resposta:
"""

        try:
            resposta = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "gemma3:1b",
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0,
                        "num_predict": 80
                    }
                },
                timeout=30
            )

            return resposta.json()["response"].strip()

        except Exception as erro:
            return f"Erro ao conectar com a IA: {erro}"