def area(a, b):
    """

    :param a: comprimento
    :param b: largura
    :return: area do tereno
    """
    c = a*b
    print(f'A area de um terreno {a}x{b} é {c:.2f}M².')
def contador(a, b, c):
    import time
    if c < 0:
        c *= -1
    elif c == 0:
        c += 1
    if b < a:
        c = c-(c*2)
        b -= 2
    for i in range(a, b+1, c):
        print(i, end=' ')
        time.sleep(0.30)
    print('fim')
def fatorial(num=1,show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c,end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ', end='')
        f *= c
    return f
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
def maior(* núm):
    cont = maior = 0
    print('\nverificando os valores...')
    for i in núm:
        cont +=1
        print(i,end=' ')
        if cont == 0:
            maior = i
        else:
            if i > maior:
                maior = i
    print(f'Foram informados {cont} valores.')
    print(f'o maior valor foi {maior}')
def nota(*num, situ=False):
    n = {}
    n['total'] = len(num)
    n['maior'] = max(num)
    n['menor'] = min(num)
    n['media'] = sum(num) / len(num)
    if situ:
        if n['media'] >= 7:
            n['situação'] = 'boa'
        elif n['media'] >= 5:
            n['situação'] = 'razoavel'
        else:
            n['situação'] = 'ruim'
    return n
def sorteio(lista):
    print('Sorteando numeros',end=' ')
    for i in range(0, 5):
        sleep(0.5)
        a = randint(1, 10)
        lista.append(a)
        print(a,end=' ')
    print('Prontoo')
def par(lista):
    a = 0
    for nume in lista:
        if nume % 2 == 0:
            a+=nume
        sleep(0.1)
    print(f'A soma dos numeros pares foi {a}')
def voto(a):
    """
    Calcula se a pessoa tem direito de voto.
    :param a: Ano de nacimento.
    :return: a possibilidade de voto.
    """
    from datetime import date
    data = date.today().year
    a = data - a
    if a < 16:
        return f'{a}: voto negado.'
    elif 16 <= a < 18 or a > 65:
        return f'{a}: voto opcional.'
    else:
        return f'{a}: voto obrigatorio.'
def gol(a='', b=''):
    if a == '':
        a = "'desconhecido'"
    if b == '':
        b = 0
    return f'O jogador {a} fez {b} gol(s).'