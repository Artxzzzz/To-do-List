def showList(lista):
    toReturn = []
    
    for idx, item in enumerate(lista): # Listar o item e o id
        toReturn.append(f"[{idx+1}] - {item.name}") # Formatar como o exemplo: [1] - Fazer lição de casa
    
    return toReturn