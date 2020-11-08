from random import randint
from time import sleep
from operator import itemgetter
jogadores= {'Jogador 1': randint(1, 6),
            'Jogador 2': randint(1, 6),
            'Jogador 3': randint(1, 6),
            'Jogador 4': randint(1, 6)}

for k , v in jogadores.items():
    print (f'O {k} jogou {v}')
    sleep(1)
ranking = []
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('#='*30)
for k , v in enumerate(ranking):
    print(f'{k+1}º Luga: {v[0]} com {v[1]}')
    sleep(1)
print('#='*30)
