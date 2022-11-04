import character, numeros

ma = me = 0
x = numeros.leiaint('Quantos números vai digitar ')
for x in range (x):
    n = numeros.leiaint('Digite um número ')
    if n == 1 :
        ma = n
        me = n
    else:
        if n>ma :
            ma = n
            if n< me:
                me = n
print(f'O maior é {ma}')
print(f'O menor é {me}')