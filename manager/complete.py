from .config import log

def complete(item, itemslist):
    itemslist[item].completeModule()
    log.makeLog(item, "COMPLETE ITEM")

    return itemslist