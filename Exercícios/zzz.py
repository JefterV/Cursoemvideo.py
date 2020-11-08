total = 0
produto = 0
cont = 0
sem = 0
resp = ' '
barato =''
while resp not in 'N':
    nome = str(input('Digite o nome: '))
    preço = float(input('Digite o valor: '))
    cont += 1
    total += preço
    if preço >= 1000:
        produto += 1
    if cont == 1 or preço < sem:
        menor = preço
        barato =nome
    resp = str(input('Deseja continuar [S/N]: ')).upper()[0]

print('Encerrando')
print(f'O total que foi gasto é R$: {total:.2f}')
print(f'{produto} produtos custam mais que 1000')
print(f'n {barato} x {menor:.2f}')