from packages import utils

def showList(lista):
    toReturn = []
    

    for idx, item in enumerate(lista): # Listar o item e o id
        match item.complete:
            case True:
                toReturn.append(f"{idx+1} - [✓] - {utils.risk(item.name)}") 
            case False:
                toReturn.append(f'{idx+1} - [X] - {item.name}') # Formatar como o exemplo: 1 - [X] - Fazer lição de casa
    return toReturn