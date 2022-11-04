import character, numeros

character.func()
dt = numeros.leiaint('Dias trabalhados: ')
hr = numeros.leiafloat('Horas trabalhadas: ')
t = dt*hr
print(f'Seu total de horas trabalhadas é de {float(t):.1f} horas')
tg =t*25
print(f'O total a receber é de R$ {tg:.2f}')