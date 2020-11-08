from random import randint
from time import sleep
print('#='*60)
print(f'{"LOTERICA SALVADOR":^120}')
print('#='*60)
num = int(input('Quantos jogos você quer: '))
lista= []
jogos= []
for c in range(0, num):
    contador = 0
    while True:
        var = randint(1, 60)
        if var not in lista:
            lista.append(var)
            contador += 1
        if contador == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()

for p , e in enumerate(jogos):
    print(f'{p+1}º Jogo: {e}')
    sleep(1.5)



