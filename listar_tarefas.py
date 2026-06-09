from data.database import conectar

conn = conectar()
cursor = conn.cursor()

cursor.execute("SELECT * FROM tarefas")

for tarefa in cursor.fetchall():
    print(tarefa)

conn.close()type menus.py