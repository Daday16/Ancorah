from data.database import conectar

try:
    conn = conectar()
    print("Conectado ao MySQL!")
    conn.close()

except Exception as erro:
    print("Erro:", erro)