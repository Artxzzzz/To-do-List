def showList(lista):
    toReturn = []
    
    for item in lista:
        toReturn.append(f"[{item.idx}] - {item.name}")
    
    return toReturn