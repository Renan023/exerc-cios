import character, numeros

n = character.leiachar('Nome ')
s = character.leiachar('Sexo[M/F] ').strip().upper()
while s not in "MmFf":
    s = character.leiachar('Sexo[M/F] ').strip().upper()
v = numeros.leiafloat('Valor ')
if s not in 'Mm':
    desc15 = v * 85/100
    print(f'O desconto de {n} será de {desc15:.2f}')
else:
    desc3 = v* 97/100
    print(f'O desconto de {n} será de {desc3:.2f}')