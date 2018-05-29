def input_int(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print('\nNúmero invalido.')


def desconto():
    valor = input_int('\nQual o valor do produto? R$')
    desconto = input_int('\nQuanto é o desconto? ')
    resultado = valor - ((valor*desconto)/100)
    print('O cliente terá que pagar R${:.2f}\n'
          '----------------------------\n'
          'O produto de R${:.2f} com desconto de {}% custará R${:.2f}\n'.format(resultado, valor, desconto, resultado))