import uuid
from datetime import datetime


def gerar_id():
    return str(uuid.uuid4())


def horario_atual():
    return datetime.now().strftime("%H:%M:%S")