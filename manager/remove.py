from .config import log

def remove(idx: int, itemslist: list): # Método de remover item
    log.makeLog(itemslist[idx], "REMOVE ITEM")
    itemslist.pop(idx) # Remover o id especificado
    
    return itemslist # Retornar lista