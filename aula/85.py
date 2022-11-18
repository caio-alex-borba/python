n = [[], []]
perg = 0
cont = 1
while cont != 8:
    perg = (int(input(f'digite o {cont}º numero: ')))   #aprovisiono em uma variavel
    if perg % 2 == 0:          # sendo divisiveu por 2 mando para lista 0
        n[0].append(perg)
    elif perg % 2 == 1:       #nao sendo mando para lisa 1
        n[1].append(perg)
    cont += 1
n[0].sort()             # ordena os numereos da primeira lis
n[1].sort()             # e esse o da segunda
print(f'os numeros pares foram {n[0]}')
print(f'os numeros impares foram {n[1]}')