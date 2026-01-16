from .. import utils

def additem(itemsList: list) -> list:
    itemName = input("Qual é o item que você quer adicionar? ")

    horario, data = utils.getTime()

    template = {
        "Name": itemName,
        "Horario": horario,
        "Data": data,
        "Id": len(itemsList)+1
    }
    
    itemsList.append(template)
    return itemsList