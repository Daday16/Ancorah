from data.database import conectar

conn = conectar()
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO tarefas (titulo) VALUES (%s)",
    ("Estudar TCC",)
)

conn.commit()
conn.close()

print("Tarefa salva!")