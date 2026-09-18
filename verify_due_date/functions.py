from datetime import datetime

def today():
    today_date = datetime.now().date()
    return today_date

def verify_format(date):
    try:
        format = datetime.strptime(date, "%d-%m-%Y").date()
        return format
    except:
        raise Exception ("Data informada é inválida. Formato correto DIA-MÊS-ANO Ex:. 01-12-2026")   

def verify_days(due_date):
    date_format = verify_format(date=due_date)
    diference = date_format - today()
    total_days = diference.days  # .days is an attribute of the timedelta object.
    if total_days == 0:
        return 'O produto vence hoje.'
    elif total_days < 0:
        return f'O produto está a {abs(total_days)} dias vencido.'
    else:
        return f'Faltam {total_days} dias para o vencimento.'