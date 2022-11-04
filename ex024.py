import numeros, character

km = numeros.leiafloat('Quantos Km vai percorrer ')
if km == 200:
    vkm = km *0.50
    print(f'Será percorrido {km} o valor ficará R$ {vkm:.2f}')
else:
    vkm = km * 0.45
    print(f'Será percorrido {km} o valor será de R$ {vkm:.2f}')
character.menu('Até logo')