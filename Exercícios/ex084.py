listagem = [[], []]
for c in range(0, 4):
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))
    listagem[0].append(nome)
    listagem[1].append(peso)
print('='*60)
for c, p in enumerate(listagem[0]):
    if listagem[1][c] <= 70:
        print(f'{p} está no peso ideal {listagem[1][c]}kg')
    else:
        if listagem[1][c] >= 80 and listagem[1][c] <= 100:
            print(f'{p} está um pouco acima do peso {listagem[1][c]}kg')
        elif listagem[1][c] > 100:
            print(f'{p} você está muito acima do peso {listagem[1][c]}kg')
print('='*60)
variavel1= listagem[1].index(min(listagem[1]))
print(f'O menor peso foi {min(listagem[1])}kg de {listagem[0][variavel1]}')
variavel1= listagem[1].index(max(listagem[1]))
print('='*60)
print(f'O maior peso foi de {max(listagem[1])}kg de {listagem[0][variavel1]}')
print('='*60)