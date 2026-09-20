from functions import *
import os

nome = input('Qual o seu nome? ').title().strip()
date_birth = input('Qual sua data de aniversário? (dd/mm/aaaa) ')

os.system('cls' if os.name == 'nt' else 'clear')

date_birth =  verify_format(date=date_birth)

if date_birth:
   
    print(f'Olá, {nome}!')

    idade_user = idade(date_birth)
    print(f'Você tem {idade_user} anos.')

    day_week = day_of_the_week(date_birth=date_birth)
    print(f'Você nasceu em um(a) {day_week}')

    days_for_next = days_until_the_birthday(date_birth=date_birth)
    if days_for_next == 0:
        print(f'Parabéns, {nome}. Hoje é dia de festejar. 🎂🎉')
    else:
        print(f'Faltam {days_for_next} dias para o seu próximo aniversário.')
else:
    print('Formato de data inválido! Siga o exemplo (Ex: 16/04/2005).')