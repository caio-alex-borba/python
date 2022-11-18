while True:
    n = int(input('numero ou 0 para sair: '))
    if n % 2 == 0:
        print('é par')
    elif n % 2 == 1:
        print('não é par')
    if n == 0:
        break