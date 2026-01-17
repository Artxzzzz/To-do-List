from packages import models, utils
from .config import log

def add(itemslist: list, name: str) -> list:
    horario, data = utils.getTime()
    
    item = models.item(name=name, hour=horario, date=data)
    itemslist.append(item)

    log.makeLog(item, "ADD ITEM")

    return itemslist

