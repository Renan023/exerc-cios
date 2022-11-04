import character, numeros
from datetime import datetime

at = datetime.today().year
x = numeros.leiaint('Cadastros: ')
for x in range(x):
    f = 0
    nome = character.leiachar('Nome: ')
    nasc = numeros.leiaint('Nascimento: ')
    idade = at - nasc
    print(f'{nome} ,{idade} anos')
    if idade < 18:
        f = 18 - idade
        print(f'Faltam {f} anos para {nome} se alistar')
    else:
        p = idade - 18
        print(f'Já passou {p} anos que {nome} se alistou ')
