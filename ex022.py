from _datetime import datetime
import character, numeros
at = datetime.today().year

character.menu('Alistamento Militar'.center(50))
n = character.leiachar('Nome ')
nasc = numeros.leiaint('Ano de nascimento  ')
id = at - nasc
print(f'Idade {id} anos')

if id < 18:
    f = 0
    f = 18 - id
    print(f'{n} faltam {f} anos para se alistar ')
else:
    f= 0
    f = id - 18
    print(f'{n} se alistou faz {f} anos')