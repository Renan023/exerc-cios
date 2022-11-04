import numeros,character, datetime

at=datetime.datetime.today().year
character.cad()
nasc = numeros.leiaint('Nascimento: ')
id = at - nasc
print(f'Sua idade é de {id} anos')
if id >=18:
    print('Voto obrigatório')
else:
    print('Não precisa votar')