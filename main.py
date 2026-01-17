import ui as ui
import manager.config as config
import sys
import time
lista = []

def main(lista):
    lista = config.load()

    if lista: # Checar se a lista é válida
        toLoop = ui.showList(lista)
                
        for i in toLoop:
            print(i) # Amostrar cada item da lista
        time.sleep(0.5)
            
    while True:
        print('------------------------------------')
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

        config.save(lista)
        time.sleep(1)

if __name__ == "__main__":
    main(lista)