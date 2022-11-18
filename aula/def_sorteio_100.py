from random import randint
from time import sleep

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


numeros = []
sorteio(numeros)
par(numeros)

