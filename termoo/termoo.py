import json
import random

o = open("words.json", encoding='utf8') # o utf8 traduz os caracteres
words = json.load(o) 
chave = random.choice(list(words.keys()))

print('Advinhe o ano de lançamento do filme | Gênero: Mistério')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

tentativas = 6
victory = False

print("O filme é: " + words[chave])
while tentativas > 0 and not victory:
    res = input('Data (DDMMAAAA): ')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>')
    
    if len(res) != 8:
        print('Erro! Você precisa informar 8 digitos.')
        continue
    if res.isdigit():
        checagem = []
        pontuacao = 0
        for i in range(8):
            if res[i] == chave[i]:
               checagem.append('✅') 
               pontuacao += 1
            else:
                checagem.append('💢')
                
        print('Resposta: ')
        print('|'.join(checagem))
        print(' |'.join(res))
        
        if pontuacao == 8:
            victory = True
    else:
        print('Erro! Você precisa informar uma data.')
        continue
    tentativas -= 1 
    
if victory == True:
    print('Você venceu!')
else:
    data = f'{chave[:2]}/{chave[2:4]}/{chave[4:]}'
    print(f'Você não acertou. A data de lançamento de {words[chave]} foi em {data}')
o.close()