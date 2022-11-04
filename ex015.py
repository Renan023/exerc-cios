import character, numeros

character.menu('Programa NSMOKE'.center(50))
character.cad()
c = numeros.leiaint('Cigarros fumados por dia: ')
tc = c*10
print(f'Foi fumado em torno de {tc} minutos')
td = tc - 1440
if td <0:
    print(f'Foi perdido aproximadamente {td} horas ')
else:
    print(f'Foi perdido aproximadamente {td} dias ')