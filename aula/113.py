def leiaintero(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('Não é um valor valido')
            continue
        except KeyboardInterrupt:
            print('Valor não informado')
            return 0
        else:
            return num
def leiafloat(msg):
    while True:

        try:
            num = str(input(msg)).replace(',', '.')
            num = float(num)
        except (ValueError, TypeError):
            print('Não é um valor valido')
            continue
        except KeyboardInterrupt:
            print('Valor não informado')
            return 0
        else:
            return num


numero = leiaintero('numero inteiro: ')
n = leiafloat('numero real: ')
print(f'O valor inteiro digitado foi {numero}')
print(f'O valor real digitado foi {n}')
