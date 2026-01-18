from .config import log

def complete(idx, itemslist):
    item = itemslist[idx]
    item.completeModule()
    log.makeLog(item, "COMPLETE ITEM")

    return itemslist