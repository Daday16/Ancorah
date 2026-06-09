from data.database import conectar
from core.recompensas import adicionar_pontos


def criar_tarefa(titulo):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tarefas (titulo) VALUES (%s)",
        (titulo,)
    )

    conn.commit()
    conn.close()

    print("✅ Tarefa criada.")


def listar_tarefas():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, titulo, concluida FROM tarefas"
    )

    tarefas = cursor.fetchall()

    conn.close()

    if not tarefas:
        print("Nenhuma tarefa.")
        return []

    for i, tarefa in enumerate(tarefas):

        status = "✅" if tarefa[2] else "⏳"

        print(f"\n{i} - {tarefa[1]} [{status}]")

    return tarefas
def excluir_tarefa(indice):

    tarefas = listar_tarefas()

    try:
        id_real = tarefas[indice][0]

    except:
        print("Tarefa inválida.")
        return

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM tarefas
        WHERE id = %s
        """,
        (id_real,)
    )

    conn.commit()
    conn.close()

    print("🗑️ Tarefa excluída com sucesso!")

def concluir_tarefa(indice):

    tarefas = listar_tarefas()

    try:
        id_real = tarefas[indice][0]

    except:
        print("Tarefa inválida.")
        return

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE tarefas
        SET concluida = 1
        WHERE id = %s
        """,
        (id_real,)
    )

    conn.commit()
    conn.close()

    adicionar_pontos(10)

    print("🎉 Tarefa concluída!")


def adicionar_subtarefa(indice_tarefa, titulo):

    tarefas = listar_tarefas()

    try:
        tarefa_id = tarefas[indice_tarefa][0]

    except:
        print("Tarefa inválida.")
        return

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO subtarefas
        (tarefa_id, titulo)
        VALUES (%s, %s)
        """,
        (tarefa_id, titulo)
    )

    conn.commit()
    conn.close()

    print("✅ Subtarefa adicionada!")


def listar_subtarefas(indice_tarefa):

    tarefas = listar_tarefas()

    try:
        tarefa_id = tarefas[indice_tarefa][0]

    except:
        print("Tarefa inválida.")
        return

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, titulo, concluida
        FROM subtarefas
        WHERE tarefa_id = %s
        """,
        (tarefa_id,)
    )

    subtarefas = cursor.fetchall()

    conn.close()

    if not subtarefas:
        print("Nenhuma subtarefa.")
        return

    print("\n===== SUBTAREFAS =====")

    for i, subtarefa in enumerate(subtarefas):

        status = "✅" if subtarefa[2] else "⏳"

        print(
            f"{i} - {subtarefa[1]} [{status}]"
        )
        