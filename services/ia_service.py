import requests
import time

from data.database import conectar


class IAService:

    def perguntar(self, pergunta):

        texto = pergunta.lower()

        # ==========================
        # O QUE FAÇO AGORA
        # ==========================
        if "o que faço" in texto or "o que devo fazer" in texto:

            return self.responder_tarefas()

        # ==========================
        # TENHO TAREFAS
        # ==========================
        if "tenho tarefa" in texto or "minhas tarefas" in texto:

            return self.responder_tarefas()

        # ==========================
        # LEMBRETES
        # ==========================
        if "lembrete" in texto:

            return self.responder_lembretes()

        # ==========================
        # CANSAÇO
        # ==========================
        if "cansado" in texto or "desanimado" in texto:

            return self.responder_cansado()

        # ==========================
        # QUALQUER OUTRA PERGUNTA
        # ==========================
        return self.perguntar_ollama(pergunta)

    # =====================================================

    def responder_tarefas(self):

        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT titulo
            FROM tarefas
            WHERE concluida = 0
            LIMIT 5
        """)

        tarefas = cursor.fetchall()

        conn.close()

        if not tarefas:
            return "🎉 Parabéns! Você não possui tarefas pendentes."

        resposta = "Você possui estas tarefas pendentes:\n\n"

        for tarefa in tarefas:
            resposta += f"• {tarefa['titulo']}\n"

        resposta += "\nSugiro começar pela primeira utilizando um Pomodoro de 25 minutos."

        return resposta

    # =====================================================

    def responder_lembretes(self):

        try:

            conn = conectar()
            cursor = conn.cursor(dictionary=True)

            cursor.execute("""
                SELECT titulo
                FROM lembretes
                WHERE concluido = 0
                ORDER BY data,hora
                LIMIT 5
            """)

            lembretes = cursor.fetchall()

            conn.close()

            if not lembretes:
                return "Você não possui lembretes pendentes."

            resposta = "Você possui estes lembretes:\n\n"

            for lembrete in lembretes:
                resposta += f"• {lembrete['titulo']}\n"

            return resposta

        except:
            return "Não consegui consultar os lembretes."

    # =====================================================

    def responder_cansado(self):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM tarefas
            WHERE concluida = 0
        """)

        quantidade = cursor.fetchone()[0]

        conn.close()

        if quantidade == 0:

            return (
                "Você concluiu todas as suas tarefas. "
                "Pode descansar sem culpa! 😊"
            )

        if quantidade <= 2:

            return (
                "Falta muito pouco! "
                "Conclua mais uma tarefa e depois faça uma pausa."
            )

        return (
            "Não tente fazer tudo de uma vez.\n"
            "Escolha apenas uma tarefa simples e faça um Pomodoro de 10 minutos."
        )

    # =====================================================

    def perguntar_ollama(self, pergunta):

        prompt = f"""
Você é a TPAC, uma assistente inteligente de produtividade.

REGRAS:

- Responda somente em português.
- Seja simpática.
- Seja objetiva.
- Máximo 5 frases.
- Sempre incentive uma ação prática.
- Nunca diga que é uma IA.
- Nunca peça mais detalhes.

Pergunta:

{pergunta}

Resposta:
"""

        inicio = time.time()

        try:

            resposta = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "phi3:latest",
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.2,
                        "num_predict": 80
                    }
                },
                timeout=60
            )

            tempo = time.time() - inicio

            print(f"\nTempo da IA: {tempo:.2f} segundos\n")

            dados = resposta.json()

            if "response" in dados:
                return dados["response"].strip()

            if "error" in dados:
                return dados["error"]

            return "Não consegui responder."

        except Exception as erro:

            return f"Erro ao acessar a IA: {erro}"