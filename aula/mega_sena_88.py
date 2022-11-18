from random import randint
sena = []
jogos = int(input('Quandos jogos deseja sortear? '))
temp = []
for i in range(jogos):
    for e in range(6):
        temp.append(int(randint(0, 60)))
    temp.sort()
    sena.append(temp[:])
    temp.clear()
print('sorteando jogos')
for a, b in enumerate(sena):           # pega a posição e o artigo dessa posição
    print(f'jogo N°{a+1}: {b}')
