def options():
    """Aqui é as opções de o que fazer na lista"""
    opt = {
        "Adicionar item": 1,
        "Remover item": 2,
        "Completar item": 3
    }

    for k, v in opt.items(): # Loop que amostra todas as opções
        print(f'[{v}] - {k}') # Formatar para ficar igual esse exemplo: "[1] - Adicionar item"

    escolha = ''
    while True:
        escolha = input("Digite sua escolha: ").lower() # Pedir escolha
        validText = not escolha.isdigit() and escolha in [item.lower() for item in opt.keys()] # Validar se a escolha está como opção
        validNumber = escolha.isdigit() and int(escolha) in opt.values() # Validar se o número está como id da opção

        if validText or validNumber:
            break # Quebrar o loop se estiver válido

        print("Escolha inválida, tente novamente") # Erro de estar inválido
            
    
    for k, v in opt.items(): # Tratar escolha pra ser número
        if escolha == k.lower():
            escolha = v
    
    match int(escolha):
        case 1:
            """Lógica de adicionar"""
            print(1)
        case 2:
            """Lógica de remover"""
            print(2)
        case 3:
            """Lógica de completar"""
            print(3)
            

if __name__ == "__main__":
    options()