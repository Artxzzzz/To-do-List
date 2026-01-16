from ..manager import add

def additem(itemsList: list) -> list: # Função de adicionar item
    itemName = input("Qual é o item que você quer adicionar? ") # Perguntar nome do item

    itemsList = add(itemsList, itemName) # Adicionar a lista usando o método "Add()"

    return itemsList # Retorna lista modificada