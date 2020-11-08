from random import randint

numeros = []
def sortear(self):
    cont = 0
    while cont <= 4:
        numeros.append(randint(1, 100))
        cont += 1
    print(f'Os numeros sorteados são: {numeros}')
def pares(lista):
    conta = 0
    for valor in lista:
        if valor % 2 == 0:
            conta +=valor
    print(f'A soma dos numeros pares é = {conta}')


numeros = []
sortear(numeros)
pares(numeros)
