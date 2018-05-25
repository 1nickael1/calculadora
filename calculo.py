def opcoes():
    opcao = int(input('\nQual operação deseja fazer?'
                      '\n1 - Adição         5 - Potência'
                      '\n2 - Subtração      6 - Divisão Inteiro'
                      '\n3 - Divisão        7 - Resto da Divisão'
                      '\n4 - Multiplicação  8 - Raiz Quadrada'
                      '\n                   9 - Sair\n\n'))
    if opcao < 1 or opcao > 9:
        print('\nEssa opção não existe!')
        opcoes()
    elif opcao == 1:
        soma()
    elif opcao == 2:
        subt()
    elif opcao == 3:
        divi()
    elif opcao == 4:
        multi()
    elif opcao == 5:
        pote()
    elif opcao == 6:
        inte()
    elif opcao == 7:
        resto()
    elif opcao == 8:
        raiz()
    elif opcao == 9:
        print('\nSaindo do programa!')
        exit()


def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('Número invalido.')
        except ZeroDivisionError:
            print('nao divisivel por 0')


def soma():
    n1 = input_int('\nDigite o primeiro número: ')
    n2 = input_int('\nDigite o  segundo número: ')
    print('\nA adição de {} em {} é {}\n'.format(n1, n2, (n1 + n2)))


def subt():
    n1 = input_int('\nDigite o primeiro número: ')
    n2 = input_int('\nDigite o  segundo número: ')
    print('\nA Subtração de {} e {} é {}\n'.format(n1, n2, (n1 - n2)))


def divi():
    n1 = input_int('\nDigie o primeiro número: ')
    n2 = input_int('\nDigite o segundo número: ')
    print('\nA Divisão de {} e {} é {}\n'.format(n1, n2, (n1 / n2)))


def multi():
    n1 = input_int('\nDigite o primeiro número: ')
    n2 = input_int('\nDigite o  segundo número: ')
    print('\nA Multiplicação de {} e {} é {}\n'.format(n1, n2, (n1 * n2)))


def pote():
    n1 = input_int('\nDigite o primeiro número: ')
    n2 = input_int('\nDigite o  segundo número: ')
    print('\nO {} elevado a potência {} é {}\n'.format(n1, n2, (n1 ** n2)))


def inte():
    n1 = input_int('\nDigite o primeiro número: ')
    n2 = input_int('\nDigite o  segundo número: ')
    print('\n A divisão inteira de {} e {} é {}\n'.format(n1, n2, (n1 // n2)))


def resto():
    n1 = input_int('\nDigite o primeiro número: ')
    n2 = input_int('\nDigite o  segundo número: ')
    print('\nResto da divisão de {} e {} é {}\n'.format(n1, n2, (n1 % n2)))


def raiz():
    n1 = input_int('\nDigite o número: ')
    print('\nA raiz quadrada de {} é {:.3f}\n'.format(n1, (n1 ** (1 / 2))))
