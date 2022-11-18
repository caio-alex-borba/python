from termcolor import colored

n = int(input('digite um numero: '))
for i in range(0, 11):
    print(f'{n}x{i}= ', end=' ')
    print(colored(n * i, 'red'))