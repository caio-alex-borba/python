from random import randint # o pc pensa em um numero
from termcolor import colored
pc = randint(0, 10)
print('Vou pensar em um numero, tente adivinhar....')
eu = int(input('\nVamos la digite um numero. '))
t = 1
while eu != pc:
    eu = int(input('Foi quase, tente outa vez. '))
    t = t + 1
print(f'\nIsso ai você acertou com {t} tentativas.')

