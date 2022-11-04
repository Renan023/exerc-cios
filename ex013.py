import character, numeros

character.menu('Locadora de carros OrangeSpitz'.center(50))
km = numeros.leiafloat('KM percorridos: ')
dias = numeros.leiaint('Dias alugados:')
td = dias*90
tkm = km *.20
print(f'Por dia(s) alugado(s) o valor é de R$ {td:.2f} e KM percorridos R${tkm:.2f}')
tt = td +tkm
print(f'Totalizando um valor de R$ {tt:.2}')