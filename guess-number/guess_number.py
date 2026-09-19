import random

n = input('Informe até qual número o sorteio pode ser realizado: ')

if n.isdigit(): # verifica se a str tem somente números inteiros positivos.
    n = int(n)
else:
    print('ERRO: Valor informado não é númerico. Tente novamente informando um número.')
    quit()
   
sorteio = random.randint(0,n)
tentativas = 0
while True:
    x = input('Tente acertar o número: ')
    
    if x.isdigit():
        x = int(x)
    else:
        print('ERRO: Valor informado não é númerico. Informe um número.')
        continue
    tentativas += 1
    if x == sorteio:
        print(f'Parábens!Você acertou. | Tentativas: {tentativas}')
        break
    else:
        print('Você errou. Tente novamente')
        if x > sorteio:
            print(f'Dica: {x} é maior')
        else:
            print(f'Dica: {x} é menor')