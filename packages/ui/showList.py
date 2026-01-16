from .. import utils

def showList(lista):
    toReturn = []
    
    for idx, item in enumerate(lista): # Listar o item e o id
        match item.complete:
            case True:
                toReturn.append(f"{idx+1} - [✓] - {utils.risk(item.name)}") # Formatar como o exemplo: [1] - Fazer lição de casa
            case False:
                toReturn.append(f'{idx+1} - [X] - {item.name}')
    return toReturn