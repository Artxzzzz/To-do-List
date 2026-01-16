from manager import complete

def completeitem(itemslist: list):

    while True:
        toComplete = input("Qual item você quer completar? ") # Pergunta
        if toComplete.isdigit(): # Se for digito
            idx = int(toComplete)-1 # Index é o toComplete - 1

            if 0 <= idx < len(itemslist): # Garante se o index está entre 0 e o maior número de itemslist
                break # Quebre o loop

        print("Esse item é invalido, tente novamente") # Se o loop não quebrou, imprima isso e volte para o começo

    return complete(idx, itemslist) # Retorne o retorno do método complete()