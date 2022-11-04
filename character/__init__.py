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
