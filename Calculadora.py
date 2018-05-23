#faça as alterações no branch dev

from calculo import opcoes

print('Bem vindo a calculadora!')


opcoes()
i = 0
while i == 0:
    x = int(input('Deseja fazer outra conta?\n1 - Sim\n2 - Não'))
    if (x == 1):
        opcoes()
    else:
        print('saindo')
        i = i + 1
