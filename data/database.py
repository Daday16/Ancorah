import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv(override=True)


def conectar():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )


def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(255) NOT NULL,
        concluida BOOLEAN DEFAULT FALSE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subtarefas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        tarefa_id INT NOT NULL,
        titulo VARCHAR(255) NOT NULL,
        concluida BOOLEAN DEFAULT FALSE,
        FOREIGN KEY (tarefa_id)
        REFERENCES tarefas(id)
        ON DELETE CASCADE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        pergunta TEXT,
        resposta TEXT,
        data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def adicionar_tarefa(titulo):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tarefas (titulo) VALUES (%s)",
        (titulo,)
    )

    conn.commit()
    conn.close()


def listar_tarefas():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tarefas")

    tarefas = cursor.fetchall()

    conn.close()

    return tarefas


def concluir_tarefa(id_tarefa):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tarefas SET concluida = TRUE WHERE id = %s",
        (id_tarefa,)
    )

    conn.commit()
    conn.close()


def remover_tarefa(id_tarefa):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tarefas WHERE id = %s",
        (id_tarefa,)
    )

    conn.commit()
    conn.close()


def salvar_conversa(pergunta, resposta):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO conversas (pergunta, resposta)
        VALUES (%s, %s)
        """,
        (pergunta, resposta)
    )

    conn.commit()
    conn.close()


def listar_conversas():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
    SELECT *
    FROM conversas
    ORDER BY data_criacao DESC
    """)

    dados = cursor.fetchall()

    conn.close()

    return dados