from datetime import datetime
from time import sleep

from win11toast import toast
from data.database import conectar


def monitorar_lembretes():

    while True:

        try:

            agora = datetime.now()

            conn = conectar()
            cursor = conn.cursor(dictionary=True)

            cursor.execute("""
                SELECT *
                FROM lembretes
                WHERE notificado = 0
            """)

            lembretes = cursor.fetchall()

            for lembrete in lembretes:

                data_hora = datetime.combine(
                    lembrete["data"],
                    datetime.min.time()
                ) + lembrete["hora"]

                if agora >= data_hora:

                    toast(
                        title="TPAC",
                        body=f"🔔 Hora de: {lembrete['titulo']}",
                        duration="long"
                    )

                    print(
                        f"\n🔔 Lembrete '{lembrete['titulo']}' foi enviado e está em Lembretes Pendentes."
                    )

                    cursor.execute("""
                        UPDATE lembretes
                        SET
                            notificado = 1,
                            pendente = 1
                        WHERE id = %s
                    """, (lembrete["id"],))

            conn.commit()
            conn.close()

        except Exception as erro:
            print("Erro no monitor:", erro)

        sleep(10)