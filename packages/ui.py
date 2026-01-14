from packages import utils
import time

def additem(itemsList: list) -> list:
    itemName = input("Qual é o item que você quer adicionar? ")

    horario, data = utils.getTime()

    template = {
        "Name": itemName,
        "Horario": horario,
        "Data": data,
        "Id": len(itemsList)+1
    }
    
    itemsList.append(template)
    return itemsList

def options(itemsList) -> int:
    """Aqui é as opções de o que fazer na lista"""
    opt = {
        "Adicionar item": 1,
        "Remover item": 2,
        "Completar item": 3,
        "Sair": 4,
    }
    print("\n")
    for k, v in opt.items(): # Loop que amostra todas as opções
        print(f'[{v}] - {k}') # Formatar para ficar igual esse exemplo: "[1] - Adicionar item"

    escolha = ''
    while True:
        escolha = input("Digite sua escolha: ").lower() # Pedir escolha
        validText = not escolha.isdigit() and escolha in [item.lower() for item in opt.keys()] # Validar se a escolha está como opção
        validNumber = escolha.isdigit() and int(escolha) in opt.values() # Validar se o número está como id da opção
        suf = False

        for k, v in opt.items(): # Ver se a escolha corresponde ao valor de itemsList
            if escolha == k.lower() or validNumber and int(escolha) == v:
                if not itemsList and v in (2, 3):
                    print("Você não tem items suficientes para fazer isso.")
                    suf = True
        if validText or validNumber and not suf:
            break # Quebrar o loop se estiver válido
        
        if not suf: # Se tiver itens suficientes e o loop estiver rodando
            print("Escolha inválida, tente novamente") # Erro de estar inválido
        
        time.sleep(0.1)
    
    for k, v in opt.items(): # Tratar escolha pra ser número
        if escolha == k.lower():
            escolha = v
    
    return escolha
            

def showList(lista):
    toReturn = []
    
    for item in lista:
        toReturn.append(f"[{item['Id']}] - {item['Name']}")
    
    return toReturn

if __name__ == "__main__":
    options([])