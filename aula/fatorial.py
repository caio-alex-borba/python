n = int(input('Digite um numero para saber seu fatorial: '))
c = n
f = 1
while c > 0:
    f *= c
    c -= 1
print(f'o fatorial de {n} é {f}')
