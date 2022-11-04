import math, time
a = list()
for c in range(3):
    a.append(int(input('Qual os valores da equação de segundo grau ')))
print(f'{a[0]}x²+{a[1]}x+{a[2]} ')
print(f'Δ = {a[1]}²-4.{a[0]}.{a[2]}')
delta = (a[1]**2)-4*(a[0]*a[2])
print(f'Δ = {delta}')
if delta <0:
    print('Não é possivel terminar a equação. Pois deu resultado negativo.... ')
else:
    print('Vamo prosseguir...')
    time.sleep(0.2)
rq = math.sqrt(delta)
print(f'x = -{a[1]}+√{delta}/2.{a[0]}')
print(f'x = {(-a[1]+rq)/2*a[0]:.0f}')
print(f'x = -{a[1]}-√{delta}/2.{a[0]}')
print(f'x = {(-a[1]-rq)/2*a[0]:.0f}')