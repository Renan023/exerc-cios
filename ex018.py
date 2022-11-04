import numeros, character

soma = c = 0
character.cad()
x = numeros.leiaint('Avaliações ')
for x in range(x):
    n = numeros.leiafloat('Nota ')
    soma +=n
    c+=1
    m= soma/c
print(f'A média do aluno é {m} ')
if m >=7:
    print(f'Sua média é de {m} . Pode seguir para o próximo semestre ')
else:
    print(f'Sua média é de {m} . Foi reprovado')
