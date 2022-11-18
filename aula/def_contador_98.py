
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

def txt():
    print('#'*30)


txt()
print('De 10 até 1, de 1 em 1.')
contador(1, 10, 1)
txt()
print('De 10 até 0, de 2 em 2:')
contador(10, 0, -2)
txt()
print('Agora é sua vez.')
contador(int(input('inicio')), int(input('fim')), int(input('passo')))
txt()