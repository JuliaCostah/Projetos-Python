from functions import *
import os

name = []
distance = []
valor = []

while True:

    print('------ SISTEMA DE CADASTRO ------\n')
    print('[1] Registrar novo frete\n[2] Fechar o caixa (gerar relatório)')
    print('[3] Encerrar o sistema')
    
    esc = verify_choice()
    if esc == 3:
        print('Saindo...')
        break
    
    if esc == 1:
        while True:
            name_driver = input('Nome do motorista: ').title().strip()
            name.append(name_driver)
            
            distance_traveled = float(input('Distância percorrida (Km): '))
            distance.append(distance_traveled)
            
            valor_frete = float(input('Valor cobrado no frete: R$ '))
            valor.append(valor_frete)
            
            n = input('Quer continuar cadastrando? [S/N]').upper()
            
            os.system('cls' if os.name == 'nt' else 'clear')   
            
            if n != 'S':
                print('Cadastros realizados com sucesso. Relatório já pode ser gerado.')
                break
            else:
                continue
    
    if esc == 2:
        print('===== Relatório de viagens e fretes =====\n')
        if name and distance and valor:
            
            faturamento_total = sum(valor)
            maior_viagem = max(distance)
            media_frete = faturamento_total/len(valor)
            melhores_motoristas = []
            
            cont = 0
            print(f'   {"Motorista":<12} | {"Distância":<12} | {"Valor":<12}\n')
            for x,y,z in zip(name,distance,valor):
                dist = f'{y} Km'
                print(f'{cont + 1:2} {x:<12} | {dist:<12} |  R$ {z:.2f}')
                cont += 1
            
            for i,c in zip(name,distance):
                if c == maior_viagem:
                    melhores_motoristas.append(i)
                    
            print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
            
            print(f'Faturamento Total: R$ {faturamento_total:.2f}\nViagem mais longa: {', '.join(melhores_motoristas)} ({maior_viagem} Km)')
            print(f'Valor médio dos fretes diários: R$ {media_frete:.2f}')
            
            print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        else:
            print('Nenhum cadastro realizado ainda. Para cadastrar escolha 1.')
            continue