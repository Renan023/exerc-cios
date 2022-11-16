import datetime, numeros , character


def menu(msg):
    print('='*50)
    print(msg)
    print('='*50)


def leiachar(char):
    while True:
        try:
            char = input(char)
        except (KeyboardInterrupt):
            print('\n\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return char


def func():
    menu('FICHA DE FUNCIONÁRIO'.center(50))
    nome = leiachar('Nome do funcionário: ')
    s = leiachar('Sexo [M/F] ').strip().upper()[0]
    while s not in 'MmFf':
        print('\033[31mErro digite novamente\033[m')
        s = leiachar('Sexo [M/F] ').strip().upper()[0]


def cad():
    nome = leiachar('Nome: ')
    s = leiachar('Sexo [M/F] ').strip().upper()[0]
    while s not in 'MmFf':
        print('\033[31mErro digite novamente\033[m')
        s = leiachar('Sexo [M/F] ').strip().upper()[0]


def nome():
    print('='*50)
    nome = input('Nome ')

def idade():
    at =datetime.datetime.today().year
    nasc = numeros.leiaint('Ano de nascimento: ')
    id = at - nasc
    print(f'Idade: {id} anos ')


def sexo():
    while True:
        try:
            sexo = character.leiachar('Sexo: ').strip().upper()[0]
            while sexo not in 'MmFf':
                print('\033[31mDigite novamente um sexo válido\033[m')
                sexo = character.leiachar('Sexo: ').strip().upper()[0]
        except (KeyboardInterrupt):
                print('\033[31mInterrompido pelo usuário\033[m')
        else:
            return sexo

def s_n():
    while True:
        try:
            s_n = leiachar('Bonificação[S/N] ').strip()[0]
            while s_n not in 'SsNn':
                print(f'\033[31mDigite novamente\033[m')
                s_n = leiachar(s_n).strip()[0]
        except (KeyboardInterrupt):
            print('\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return s_n
