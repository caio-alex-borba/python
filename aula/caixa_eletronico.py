from termcolor import colored
print(colored('~'*45,'blue'))
print(colored('~'*10,'blue'),colored('BEM VINDO AO BAMERINDOS','red'),colored('~'*10,'blue'))
valor = int(input(colored('valor a sacar R$ ','green')))
cedula = 100
notas = 0

while True:
    if valor >= cedula:
        valor -= cedula
        notas += 1
    else:
        print(colored(f'Você sacou {notas} notas de R${cedula}','yellow'))
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        notas = 0
        if valor == 0:
            break