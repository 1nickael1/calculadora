from calculo import opcoes
from tabuada import conta
from porcentagem import desconto

print('Bem vindo!\n')


def principal():
    z = 0
    while z == 0:
        y = int(input('Escolha a ferramente que deseja usar!\n'
                      '1 - Calculadora\n'
                      '2 - Tabuada\n'
                      '3 - Porcentagem\n'
                      '4 - Sair\n'))
        if y < 1 or y > 4:
            z = 0
        elif y == 1:
            opcoes()
            z = z + 1
        elif y == 2:
            conta()
            z = z + 1
        elif y == 3:
            desconto()
            z = z + 1
        else:
            print('Fechando programa!')
            exit()

principal()

i = 0
while i == 0:
    x = int(input('Deseja escolher outra opção?\n1 - Sim\n2 - Não\n\n'))
    if x < 1 or x > 2:
        i = 0
    elif x == 1:
        principal()
    else:
        print('\nFechando Programa!')
        exit()
