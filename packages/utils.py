from datetime import datetime
import json


def getTime() -> str: # Função de conseguir o horário
    datetime_ = datetime.now() # Pegar o datetime

    data = str(datetime_.date()) # Transformar data em string
    horario = datetime_.strftime("%H:%M:%S") # Pegar horário

    return horario, data # Retornar horário e data


def risk(text: str) -> str:
    newtext = []

    for char in text:
        newtext.append(char + "\u0336")

    return ''.join(newtext)

def openJson(path) -> dict:
    with open(path, 'r') as f:
        return json.load(f)
    
def writeJson(path, data) -> None:
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)