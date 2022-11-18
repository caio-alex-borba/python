c = ('\033[1;42m','\033[1;44m','\033[1;97m','\033[0;0m','\033[7;30m')

def ajuda(a):
    titulo(f'acessando manual\'{a}\'',0)
    print(c[4],end='')
    help(a)
    print(c[3],end='')


def titulo(msg, cor=0):
    tam = len(msg)+4
    print(c[cor], end='')
    print('#'*tam)
    print(' ',msg)
    print('#'*tam)
    print(c[3],end='')


b = ''
while True:
    titulo('sistema de ajuda PYHelp',1)
    b = (input('  comando ou biblioteca: '))
    if b.upper() == 'FIM':
        titulo('ATE LOGO')
        break
    else:
        ajuda(b)