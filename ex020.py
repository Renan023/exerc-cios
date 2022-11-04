import numeros,character

ano = numeros.leiaint('Ano ')
if ano % 4 == 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
