import time
from random import randint
from operator import itemgetter
from time import sleep
jogo = {}
for i, a in enumerate(range(4)):
    jogo[f'jogador{i+1}'] = int(randint(0,6))

for i, a in jogo.items():
    print(f'O {i} tirou {a}')
    sleep(1)
jogo = sorted(jogo.items(), key=itemgetter(1), reverse=True)
sleep(2)
print('#'*18)
print(F'{"RANKING":^18}')
for i, a in enumerate(jogo):
    print(f'{i+1}°: {a[0]} com {a[1]}')