from random import randint
n = list()
while len(n) < 5:
    n.append(randint(0, 100)) # gera aleatorio
a = tuple(sorted(n)) # organiza mair menos
print(f'Esses foram os numeros sortiados {n} o menor foi {a[0]} e o mair {a[4]}.')





