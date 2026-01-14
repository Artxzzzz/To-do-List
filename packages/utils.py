from datetime import datetime

def getTime() -> str: # Função de conseguir o horário
    datetime_ = datetime.now()

    data = datetime_.date()
    horario = datetime_.strftime("%H:%M:%S")

    return horario, data