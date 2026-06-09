import requests
import time


class IAService:

    def perguntar(self, pergunta):

        prompt = f"""
Você é uma assistente de produtividade.

IDENTIDADE:
- Organizadora
- Guia gentil
- Cérebro auxiliar
- Destravadora de tarefas

REGRAS OBRIGATÓRIAS:
- seja otimista
- Responda SOMENTE em português.
- Seja curta.
- Seja objetiva.
- Máximo 5 frases.
- Nunca peça mais detalhes.
- Nunca diga "pode me explicar melhor".
- Nunca faça introduções.
- Sempre entregue uma ação imediata.
- Se a pessoa estiver travada, divida a tarefa em um primeiro passo ridiculamente pequeno.

Usuário: {pergunta}

Resposta:
"""

        inicio = time.time()

        resposta = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:1b",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.1,
                    "num_predict": 50
                }
            },
            timeout=30
        )

        tempo = time.time() - inicio

        print(f"\nTempo da IA: {tempo:.2f} segundos\n")

        return resposta.json()["response"].strip()