import os
print('Quiz Conhecimentos Gerais')
c = input('Quer começar? [S/N] ').upper()
if c != 'S':
    quit()

pontos = 0
print('01. Qual a montanha mais alta do mundo?\n(A) Mauna Kea\n(B) Dhaulagiri\n(C) Monte Chimborazo\n(D) Monte Everest\n(E) Pico da neblina')
res = input('Resposta: ').upper().strip()
if res == 'D':
    print(f'Você acertou!')
    pontos += 10
else:
    print('Você errou! Resposta certa: D')
print('Curiosidade: O Monte Everest tem 8.848 metros de altitude e localiza-se no Nepal, um país asiático que faz fronteira com a China e com a Índia.')
input('\nENTER para ir para próxima pergunta.')
os.system('cls' if os.name == 'nt' else 'clear')

print('\n02. Quem inventou a lâmpada?\n(A) Graham Bell\n(B) Steve Jobs\n(C) Thomas Edison\n(D) Henry Ford\n(E) Santos Dumont')
res = input('Resposta: ').upper().strip()
if res == 'C':
    print(f'Você acertou!')
    pontos += 10
else:
    print('Você errou! Resposta certa: C')
print('\nCuriosidade: A lâmpada foi inventada por Thomas Edison (1847-1931) em 1879. No dia 21 de outubro, o inventor conseguiu manter uma lâmpada acessa durante 48 horas.')

input('\nENTER para ir para próxima pergunta.')
os.system('cls' if os.name == 'nt' else 'clear')

print('\n03. Quanto tempo a Terra demora para dar uma volta completa em torno dela mesma?')
print('(A) Aproximadamente 24 horas\n(B) 365 dias\n(C) 7 dias\n(D) 365 ou 366 dias\n(E) 30 ou 31 dias')
res = input('Resposta: ').upper().strip()
if res == 'A':
    print(f'Você acertou!')
    pontos += 10
else:
    print('Você errou! Resposta certa: A')
print('Curisidade:A Terra demora aproximadamente 24 horas, mais precisamente 23 horas, 56 minutos e 4 segundos para dar uma volta completa em torno do seu próprio eixo. Esse movimento recebe o nome de rotação.')

input('\nENTER para finalizar o quiz.')
os.system('cls' if os.name == 'nt' else 'clear')
print(f'\nFim do quiz. Sua pontuação: {pontos}/30')