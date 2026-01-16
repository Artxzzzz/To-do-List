from .. import models, utils

def add(itemslist: list, name: str) -> list:
    horario, data = utils.getTime()
    
    item = models.item(name=name, hour=horario, date=data, idx=len(itemslist)+1)
    itemslist.append(item)

    return itemslist

