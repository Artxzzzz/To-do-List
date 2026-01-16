from datetime import datetime

def getTime() -> str: # Função de conseguir o horário
    datetime_ = datetime.now() # Pegar o datetime

    data = str(datetime_.date()) # Transformar data em string
    horario = datetime_.strftime("%H:%M:%S") # Pegar horário
    
    return horario, data # Retornar horário e data
