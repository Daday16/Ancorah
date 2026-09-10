from data.database import conectar
from datetime import datetime, timedelta


def criar_lembrete(titulo, data, hora):

    data_mysql = datetime.strptime(
        data,
        "%d/%m/%Y"
    ).strftime("%Y-%m-%d")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO lembretes
        (titulo, data, hora)
        VALUES (%s, %s, %s)
        """,
        (titulo, data_mysql, hora)
    )

    conn.commit()
    conn.close()

    print("\n✅ Lembrete criado com sucesso!")


def listar_lembretes():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, titulo, data, hora, concluido
        FROM lembretes
        ORDER BY data, hora
        """
    )

    lembretes = cursor.fetchall()

    conn.close()

    if not lembretes:

        print("\nNenhum lembrete cadastrado.")
        return

    print("\n===== LEMBRETES =====\n")

    for lembrete in lembretes:

        status = "✅ Concluído" if lembrete[4] else "⏳ Pendente"

        data = lembrete[2].strftime("%d/%m/%Y")
        hora = str(lembrete[3])[:5]

        print(f"ID: {lembrete[0]}")
        print(f"Título: {lembrete[1]}")
        print(f"📅 {data}")
        print(f"🕒 {hora}")
        print(f"Status: {status}")
        print("-" * 30)


def listar_pendentes():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, titulo, data, hora
        FROM lembretes
        WHERE pendente = 1
        ORDER BY data, hora
        """
    )

    pendentes = cursor.fetchall()

    conn.close()

    return pendentes


def concluir_pendente(id_lembrete):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE lembretes
        SET
            concluido = 1,
            pendente = 0
        WHERE id = %s
        """,
        (id_lembrete,)
    )

    conn.commit()
    conn.close()


def adiar_pendente(id_lembrete, minutos):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT data, hora
        FROM lembretes
        WHERE id = %s
        """,
        (id_lembrete,)
    )

    resultado = cursor.fetchone()

    if resultado is None:

        conn.close()
        return

    data = resultado[0]
    hora = resultado[1]

    data_hora = datetime.combine(
        data,
        datetime.min.time()
    ) + hora

    novo_horario = data_hora + timedelta(minutes=minutos)

    cursor.execute(
        """
        UPDATE lembretes
        SET
            data = %s,
            hora = %s,
            notificado = 0,
            pendente = 0
        WHERE id = %s
        """,
        (
            novo_horario.date(),
            novo_horario.time(),
            id_lembrete
        )
    )

    conn.commit()
    conn.close()
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                