n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
op = 0
while op != 5:
    op = str(input('\nSelecione uma opção: \n1 Somar\n2 Mutiplicar\n3 Maior\n4 Novos numeros\n5 Sair\n'))
    if op == '1':
        print(f'Resultado é {n1}+{n2}={n1 + n2}')
    elif op == '2':
        print(f'Resultado é {n1}x{n2}={n1 * n2}')
    elif op == '3':
        if n1 > n2:
            print(f'O mair numero é {n1}')
        elif n2 > n1:
            print(f'O maior numero é {n2}')
    elif op == '4':
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite um numero: '))
    elif op == '5':
        print('Valeww')
        break