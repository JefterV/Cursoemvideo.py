num = (int(input('Numeor inteiro: ')),
       int(input('Numeor inteiro: ')),
       int(input('Numeor inteiro: ')),
       int(input('Numeor inteiro: ')))
print(f'O numeros digitados foram: {num}')
print(f'O numero 9, foi digitado {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3, apareceu na posição {num.index(3)+1}')
else:
    print('O numero 3 não foi digitado.')
#print(f'Foram digitados os numeros: ', end='')
n = 0
for p in num:
    if p % 2 == 0:
        n += 1
print(f'\nForam digitados {n} pares. Eles são: ',end='')
for p in num:
    if p % 2 == 0:
        print(f'{p}...', end=' ')




