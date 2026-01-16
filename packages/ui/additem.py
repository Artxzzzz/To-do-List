from ..manager import add

def additem(itemsList: list) -> list:
    itemName = input("Qual é o item que você quer adicionar? ")

    itemsList = add(itemsList, itemName)

    return itemsList