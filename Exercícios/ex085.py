num = [[], []]
n = 's'
while n == 's':
    no = int(input('Digite um numero: '))
    if no % 2 == 0:
        num[0].append(no)
        print(f'O numero {no} foi adicionado a lista de nuemeros pares')
    elif no % 2 == 1:
        num[1].append(no)
        print(f'O numero {no} foi adicionado a lista de numeros impares')
    n = str(input('Deseja continuar [S/N]: '))
num[0].sort()
num[1].sort()
print(f'Os numeros pares digitados foram {num[0]}')
print(f'Os numeros impares digitados foram {num[1]}')