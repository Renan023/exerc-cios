import character, numeros

c=ci=0
x = numeros.leiaint('Quantos números vai registrar: ')
for x in range(x):
    n = numeros.leiaint('Qual o valor: ')
    if n % 2 == 0:
        c+=1
    else:
        ci+=1
print(f'A quantidade de valores pares é de {c}')
print(f'A quantidade de valores impares é de {ci}')