from .. import utils, models

def additem(itemsList: list) -> list:
    itemName = input("Qual é o item que você quer adicionar? ")

    horario, data = utils.getTime()
    
    item = models.item(name=itemName, hour=horario, date=data, idx=len(itemsList)+1)
    itemsList.append(item)
    return itemsList