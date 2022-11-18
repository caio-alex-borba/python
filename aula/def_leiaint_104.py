def leiaint(msg):
    """ verifica se o
    numero digitado é
    um numero inteiro
    :param msg: recebe um numero
    :return: se o numero for intero o retorna
    """
    ok = False
    valor = 0
    while True:
        numero = str(input(msg))
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print('digite somente numeros interios.')
        if ok:
            break
    return valor


numero= leiaint('numero')
print(f'Voce digitou o numero {numero}')


