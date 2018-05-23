def opcoes():
    opcao = int(input('\nQual operação deseja fazer?\n1 - soma\n2 - subtração\n3 - divisão\n4 - multiplicação\n5 - Sair\n'))
    if (opcao < 1 or opcao > 5):
        print('Essa opção não existe!')
        opcoes()
    elif (opcao == 1):
        soma()
    elif (opcao == 2):
        print('sub')
    elif (opcao == 3):
        print('div')
    elif (opcao == 4):
        print('multi')
    elif (opcao == 5):
        print('Fechando')

def soma():
    n1 = int(input('Digite o primeiro número! '))
    n2 = int(input('Digite o segundo número! '))
    print('\nA soma de {} e {} é {}\n'.format(n1, n2, (n1 + n2)))
