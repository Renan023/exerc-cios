import time, math,character


def leiafloat(f):
    while True:
        try:
            f = float(input(f))
        except (ValueError, TypeError):
            print('\033[31mDigite um número válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return f


def leiaint(n):
    while True:
        try:
            n = int(input(n))
        except (ValueError, TypeError):
            print('\033[31mDigite um número válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return n



def bissexto(ano):
    ano= leiaint(ano)
    if ano % 4 == 0 or ano % 400 == 0:
        print(f'O ano {ano} é bissexto')
    else:
        print(f'O ano {ano} não é bissexto')


def par_impar(n):
     cp = ci = 0
     n= leiaint(n)
     if n % 2 == 0:
         print(f'Número {n} é par')
         cp+=1
     else:
         print(f'Número {n} é impar')
         ci+=1
     print(f'O Total de números pares é {cp}')
     print(f'O total de números impares é {ci}')


def av_ind():
    s = c = m = 0
    x = leiaint('Avaliações ')
    for x in range(x):
        n = leiafloat('Nota ')
        s += n
        c += 1
        m = s / c
    print(f'A média do aluno é {m} ')
    if m >= 7:
        print(f'Sua média é de {m} . Pode seguir para o próximo semestre ')
    else:
        print(f'Sua média é de {m} . Foi reprovado')


def equacao():
    a= []
    for c in range(3):
        a.append(leiaint('Qual os valores da equação de segundo grau '))
    print(f'{a[0]}x²+{a[1]}x+{a[2]} ')
    print(f'Δ = {a[1]}²-4.{a[0]}.{a[2]}')
    delta = (a[1] ** 2) - 4 * (a[0] * a[2])
    print(f'Δ = {delta}')
    if delta < 0:
        print('Não é possivel terminar a equação. Pois deu resultado negativo.... ')
    else:
        print('Vamo prosseguir...')
        time.sleep(0.2)
    rq = math.sqrt(delta)
    print(f'x = -{a[1]}+√{delta}/2.{a[0]}')
    print(f'x = {(-a[1] + rq) / 2 * a[0]:.0f}')
    print(f'x = -{a[1]}-√{delta}/2.{a[0]}')
    print(f'x = {(-a[1] - rq) / 2 * a[0]:.0f}')


def media():
    xs = leiaint('Alunos: ')
    print('-'*50)
    for c in range(0, xs):
        c += 1
        nome = input(f'Aluno {c} nome: ')
        av = leiaint('Avaliações: ')
        s = 0
        m = 0
        print('='*50)
        for av in range(0, av):
            n = leiafloat('Notas: ')
            s = s + n
            m = s / (av + 1)
            sa = 0
        print(f'Aluno {c} {nome} média {m:.2f}')
        if m >= 6:
            sa = sa + m
            print(f'Aluno {c} {nome} passou com nota {m:.2f}')
            print('='*50)
        elif m >= 4 and m < 6:
            rec = 6 - m
            sa = sa + m
            print(f'Aluno {c} {nome} ficou de recuperação {m:.2f} faltou {rec:.2f}')
            print('='*50)
        else:
            rec = 6 - m
            sa = sa + m
            print(f'Aluno {c} foi retido com nota {m:.2f} faltou {rec:.2f}')
            print('='*50)
        mc = sa / xs
    time.sleep(0.4)
    print(f'A média da classe é {mc:.2f}')

def compras():
    cl = leiaint('Clientes ')
    vd = 0
    for c in range(0, cl):
        c += 1
        print(f'Cliente {c}')
        vc = leiafloat('Valor das compras ')
        pa = leiaint('Parcelas ')
        porc = leiaint('Porcentagem[desc(-)/acresc(+)] ')
        if pa == pa:
            vc1 = vc * -porc / 100
            vt = vc - vc1
            vd = vd + vt
            pt = vt / pa
            print(f'Cliente {c} valor total R$ {pt} parcelado em {pa} vezes')
    time.sleep(0.5)
    print(f'O valor de compras diárias é R$ {vd} ')


def ac_desc():
    xs = leiaint('Quantidade de funcionários ')
    for c in range(0, xs):
        c += 1
        func = character.leiachar(f'Funcionário {c} ').title()
        bonus = character.s_n()
        sal = leiafloat(f'Salário atual de {func} ')
        ac = leiaint('Acréscimo ')
        desc = leiaint('Desconto ')
        sal_desc = 0
        print('-' * 50)
        if ac > 0 or desc > 0:
            print(f'{func}')
            sal_ac = sal * ac / 100 + sal
            print(f'O salário com acréscimo de {ac}% é R$ {sal_ac:.2f}')
            sal_desc = sal_ac * desc / 100
            sal_desc = sal_ac - sal_desc
            print(f'Seu salário descontado em {desc}% fica em R$ {sal_desc:.2f}')
            print(f'O salário total do funcionário {c} {func} com seu acréscimo e desconto é de {sal_desc:.2f}')
            if bonus not in 'Ss':
                print('Próximo...')
                print('-'*50)
            else:
                pass
        if bonus not in 'Nn':
            bonus = sal_desc * 115 / 100
            print(f'O bônus de {func} totaliza o salário em R$ {bonus:.2f}')
            time.sleep(0.3)
            print('Próximo...')
            print('-'*50)