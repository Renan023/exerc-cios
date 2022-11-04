n = list()
al = input('Nome do aluno ')
for c in range(2):
    n.append(float(input('Notas ')))
print(f'{al} sua média com notas {n[0]} e {n[1]} é {(n[0]+n[1])/2}')