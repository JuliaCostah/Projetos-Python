from functions import * # * import all functions

due_date = input('Qual a data de vencimento do produto? (Ex:. 01-10-2026) ')

if len(due_date) == 10:
    print(verify_days(due_date))
else:
    print('Entrada inválida.')