from calculo import opcoes

print('Bem vindo a calculadora!')


opcoes()
i = 0
while i == 0:
    x = int(input('Deseja fazer outra equação?\n1 - Sim\n2 - Não\n\n'))
    if x < 1 or x > 2:
        i = 0
    elif x == 1:
        opcoes()
    else:
        print('\nFechando Programa!')
        i = i + 1
