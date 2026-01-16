import ui as ui
import sys
import time
import threading
lista = []

def main(lista):
    if lista: # Checar se a lista é válida
        toLoop = ui.showList(lista)
                
        for i in toLoop:
            print(i) # Amostrar cada item da lista
            
    while True:
        escolha = ui.options(lista)

        match int(escolha):
            case 1:
                """Lógica de adicionar"""
                lista = ui.additem(lista) # Adicionar a lista o item
            case 2:
                """Lógica de remover"""
                lista = ui.removeitem(lista)
            case 3:
                """Lógica de completar"""
                lista = ui.completeitem(lista)
            case 4:
                sys.exit() # Sair

        if lista: # Checar se a lista é válida
            toLoop = ui.showList(lista)
                    
            for i in toLoop:
                print(i) # Amostrar cada item da lista

        time.sleep(1)

if __name__ == "__main__":
    main(lista)