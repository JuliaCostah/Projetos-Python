import os
print('=== SISTEMAS DE NOTAS ===')

notas = []
nomes = []

while True:
    print('[1] - Cadastrar Alunos\n[2] - Exibir Relatório\n[3] - Sair')
    esc = input('O que deseja fazer? ')
    
    if esc.isdigit():
        esc = int(esc)
    else:
        print('Opção inválida.')
        continue
    
    os.system('cls' if os.name == 'nt' else 'clear')
  
    if esc != 1 and esc != 2 and esc != 3:
        print ('Escolha entre 1,2 ou 3.')
    
    if esc == 3:
        print('Saindo...')
        break
    if esc == 1:
        while True:
            nome = input('Nome do aluno (a): ').title()
            nomes.append(nome)
            
            nota = float(input('Nota do aluno (a): '))
            notas.append(nota)
            os.system('cls' if os.name == 'nt' else 'clear')
            outra = input('Quer fazer outro cadastro? [S/N]').upper().strip()
            os.system('cls' if os.name == 'nt' else 'clear')   

            if outra != 'S':
                break
            else:
                continue
        
        os.system('cls' if os.name == 'nt' else 'clear')   
        print('Notas Cadastradas. Para visualizar selecione Exibir relatório.')
           
    
    if esc == 2:
        print('=== Relatório da turma ===\n')
        if nomes and notas:
            ordenados = sorted(zip(nomes,notas))
            media = sum(notas)/len(notas)
            maior = max(notas)
            melhores = []
            z = 0
            for i, x in ordenados:
                print(f'{z + 1}. {i:<20} - Nota: {x}') # :<20 para definir a largura
                z += 1
            
            for nome,nota in zip(nomes,notas):
                if nota == maior:
                    melhores.append(nome)

            print('------------------------------------------------------')
            print(f'Média geral da turma: {media:.1f}')
            print(f"Maior nota: {', '.join(melhores)} -> {maior}")
            print('------------------------------------------------------')
        else:
            print('Nenhum aluno cadastrado ainda. Para cadastrar selecione 1.')
            continue