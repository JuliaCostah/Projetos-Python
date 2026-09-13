import random
import os

print('JOGO PEDRA - PAPEL - TESOURA')
s = input('Quer começar? [S/N]').upper()
if s != 'S':
    quit()
os.system('cls' if os.name == 'nt' else 'clear')

op = ['R','P','T']
pont_comp = 0
pont_jogador = 0
while True:
    jogador = input('Faça sua escolha [ R (Pedra) | P (Papel) | T (Tesoura)]: ').upper()
    if jogador not in op:
        print('Escolha Inválida')
        continue
    computador = random.choice(op)
    if jogador == computador:
        print(f'Empate!')
    elif jogador == 'T' and computador == 'P':
        print(f'{jogador} X {computador}')
        print('Jogador ganhou. + 1 ponto')
        pont_jogador += 1
    elif jogador == 'R' and computador == 'T':
        print(f'{jogador} X {computador}')
        print('Jogador ganhou. + 1 ponto')
        pont_jogador += 1
    elif jogador == 'P' and computador == 'R':    
        print(f'{jogador} X {computador}')
        print('Jogador ganhou. + 1 ponto')
        pont_jogador += 1
    else:
        print(f'{jogador} X {computador}')
        print(f'Computador ganhou. + 1 ponto')
        pont_comp += 1
    c = input('Enter para próxima rodada ou X para parar!').upper()
    os.system('cls' if os.name == 'nt' else 'clear')
    if c == 'X':
        print(f'Pontuação final -> Jogador {pont_jogador} X {pont_comp} Computador')
        break
if pont_jogador > pont_comp:
    print('Vitória!!! :)')
elif pont_jogador < pont_comp:
    print('Derrota!! :(')
else:
    print('Empate! :/')