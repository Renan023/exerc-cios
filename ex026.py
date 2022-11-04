import numeros

xs = numeros.leiaint('Alunos ')
for c in range(0,xs):
    c+= 1
    print(f'Aluno {c}')
    av = numeros.leiaint('Avaliações ')
    s= 0
    m = 0
    for av in range(0,av):
        n = numeros.leiafloat('Notas ')
        s = s+n
        m = s/(av+1)
        sa = 0
        mc = 0
    print(f'Aluno {c} média {m:.2f}')
    if m >= 6:
        sa = sa+m
        print(f'Aluno {c} passou com nota {m:.2f}')
    elif m>= 4 and m <6:
        rec = 6 - m
        sa= sa +m
        print(f'Aluno {c} ficou de recuperação {m:.2f} faltou {rec:.2f}')
    else:
        rec = 6 - m
        sa = sa + m
        print(f'Aluno {c} foi retido com nota {m:.2f} faltou {rec:.2f}')
    mc = sa/xs
print(f'A média da classe é {mc:.2f}')

