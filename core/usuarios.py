from data.database import conectar

def cadastrar_usuario(nome, email):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM usuarios WHERE email = %s",
        (email,)
    )

    if cursor.fetchone():
        print("\n❌ Já existe um usuário com esse e-mail.")
        conn.close()
        return False

    cursor.execute(
        """
        INSERT INTO usuarios (nome, email)
        VALUES (%s, %s)
        """,
        (nome, email)
    )

    conn.commit()
    conn.close()

    print("\n✅ Usuário cadastrado com sucesso!")
    return True