from datetime import datetime

def today():
    current_date = datetime.now().date()
    
    return current_date
    # print(current_date.strftime("%d/%m/%Y")) para exibir no formato com a barra

def verify_format(date):
    try:
        format = datetime.strptime(date, "%d/%m/%Y").date()
        return format
    except ValueError:
        return None
         

def idade(date_birth):

    idade_atual = today().year - date_birth.year 
    
    if today().month < date_birth.month:
        idade_atual -= 1
    elif today().month == date_birth.month and today().day < date_birth.day:
        idade_atual -= 1
     
    return idade_atual
    
def days_until_the_birthday(date_birth):
    
    birthday_this_year = date_birth.replace(year=today().year) 
       
    if birthday_this_year < today():
        birthday_this_year = date_birth.replace(year=today().year + 1) 
    
    days_for_next = birthday_this_year - today()
    
    total_days = days_for_next.days
    
    return total_days


def day_of_the_week(date_birth):
    
    days = [
        'Segunda-Feira','Terça-Feira','Quarta-Feira',
        'Quinta-Feira','Sexta-Feira','Sábado','Domingo'
    ]
    
    d = date_birth.weekday()
    
    return days[d]