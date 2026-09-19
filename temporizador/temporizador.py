import time
print('TEMPORIZADOR')
tempo = input('Informe o tempo (em segundos): ')

if tempo.isdigit():
    tempo = int(tempo)
else:
    print('ERRO!!Entrada inválida!')
    quit()

while tempo >= 0:
    minutes, seconds = divmod(tempo,60) # a função irá receber dois argumentos e retornar a divisão inteira e o resto.
    timer = f'{minutes:02d}:{seconds:02d}'
    print(timer,end='\r') # o \r serve para sobrescrever um print no outro.
    time.sleep(1)
    tempo -= 1
    
print("\nTEMPO FINALIZADO!!")