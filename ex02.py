from datetime import datetime

at =(datetime.today().month, datetime.today().year)
n = input('Nome ')
sl = float(input('Salário '))
print(f'{n} recebe R$ {sl:.2f} no mês {at[0]} de {at[1]}')
