n = list()
stop = 's'
while True:
    n.append(int(input('digite um numero: ')))
    stop = input('deseja continuar? S/N ')
    if stop == 'n':
        break

n.sort(reverse= True)
if n.count(5) == 1:
    print(f'voce digitou {len(n)} numeros, forao eles,{n}, e o 5 esta na sua lista')
elif n.count(5) == 0:
    print(f'voce digitou {len(n)} numeros, forao eles,{n}, e o 5 não esta na sua lista')

