from packages import models, utils

def add(itemslist: list, name: str) -> list:
    horario, data = utils.getTime()
    
    item = models.item(name=name, hour=horario, date=data)
    itemslist.append(item)

    return itemslist

