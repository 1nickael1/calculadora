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

      print('------------\n'
            '{} x  1 = {}\n'
            '{} x  2 = {}\n'
            '{} x  3 = {}\n'
            '{} x  4 = {}\n'
            '{} x  5 = {}\n'
            '{} x  6 = {}\n'
            '{} x  7 = {}\n'
            '{} x  8 = {}\n'
            '{} x  9 = {}\n'
            '{} x 10 = {}\n'
            '------------'.format(x, x, x, (x*2), x, (x*3), x, (x*4), x, (x*5), x, (x*6), x, (x*7), x, (x*8), x, (x*9), x, (x*10)))

