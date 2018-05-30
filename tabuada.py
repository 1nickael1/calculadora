def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except ZeroDivisionError:
            print('nao poe')
        except ValueError:
            print('Número invalido.\n')

def conta():
      x = input_int('Digite um numero para ver sua tabuada: ')

      for c in range(1, 11):
          print('{} x {} = {}'.format(x, c, (x * c)))
