def gol(a='', b=''):
    if a == '':
        a = "'desconhecido'"
    if b == '':
        b = 0
    return f'O jogador {a} fez {b} gol(s).'


gol()
print(gol(str(input('nome')),input('N° de gols')))