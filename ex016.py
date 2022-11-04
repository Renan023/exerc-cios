import character, numeros

character.cad()
km = numeros.leiafloat('Valor exibido dos Km no momento ultrapassado pelo radar: ')
if km <80:
    print(f'Pode prosseguir viagem!')
else:
    u = km-80
    m = u*5
    print(f'Estava a {km}Km/h, ultrapassou {u} km/h do permitido e foi multado no valor de R$ {m:.2f}')