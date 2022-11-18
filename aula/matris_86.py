l1 = [[0,0,0],[0,0,0],[0,0,0]]
p = 0

for i in range(0, 3):
    for e in range(0, 3):
        l1[i][e] = int(input(f'digite um valor para a posição [{i}, {e}]: '))

for i in range(0, 3):
    for e in range(0, 3):
        print(f'[{l1[i][e]:^5}]',end='')
        if l1[i][e] % 2 == 0:
            p +=l1[i][e]
    print()

maior = 0
for num in l1[1]:
    if num > maior:
        maior = num

print(f'A soma dos numeros pares foi {p}')
print(f'A soma da terceira coluna foi {l1[0][2] + l1[1][2] + l1[2][2]}')
print(f'O maior numero da segunda coluna foi {maior}')