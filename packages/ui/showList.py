def showList(lista):
    toReturn = []
    
    for item in lista:
        toReturn.append(f"[{item['Id']}] - {item['Name']}")
    
    return toReturn