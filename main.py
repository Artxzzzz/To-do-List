import packages.ui as controller
import sys
import time
import threading
lista = []

def main(lista):
    if lista: # Checar se a lista é válida
        toLoop = controller.showList(lista)
                
        for i in toLoop:
            print(i) # Amostrar cada item da lista
            
    while True:
        escolha = controller.options(lista)

        match int(escolha):
            case 1:
                """Lógica de adicionar"""
                lista = controller.additem(lista) # Adicionar a lista o item
            case 2:
                """Lógica de remover"""
                print(2) # Para fazer (incompleto)
            case 3:
                """Lógica de completar"""
                print(3) # Para fazer (incompleto)
            case 4:
                sys.exit() # Sair

        if lista: # Checar se a lista é válida
            toLoop = controller.showList(lista)
                    
            for i in toLoop:
                print(i) # Amostrar cada item da lista

        time.sleep(1)

if __name__ == "__main__":
    main(lista)