from manager import remove

def removeitem(itemslist: list): # Função de remover
    while True: # Loop
        itemRemove = input("Qual item você quer remover? ") # Pergunta
        if itemRemove.isdigit(): # Se for digito
            idx = int(itemRemove)-1 # Index é o itemremove - 1

            if 0 <= idx < len(itemslist): # Garante se o index está entre 0 e o maior número de itemslist
                break # Quebre o loop

        print("Esse valor é invalido, tente novamente") # Se o loop não quebrou, imprima isso e volte para o começo

    return remove(idx, itemslist) # Retorne o retorno do método remove()