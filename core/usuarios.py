from data.database import conectar


def cadastrar_usuario(nome, email):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO usuarios (nome, email)
        VALUES (%s, %s)
        """,
        (nome, email)
    )

    conn.commit()
    conn.close()

    print("✅ Usuário cadastrado com sucesso!")