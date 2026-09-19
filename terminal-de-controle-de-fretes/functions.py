import os
def verify_choice():
    
    while True:
        choice = input('Escolha uma opção: ')
        if choice.isdigit():
            choice = int(choice)
        else:
            print('Escolha entre as opções disponiveis.')
            continue
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if choice not in [1,2,3]:
            print('Escolha entre 1,2 ou 3.')
            continue
        
        return choice
        