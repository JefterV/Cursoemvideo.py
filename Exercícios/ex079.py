n = 's'
lista = list()
while n == 's':
    var = (int(input('Digite um numero: ')))
    if var in lista:
        print('Esse valor já existe... \nTente novamente.', end=' ')
    else:
        lista.append(var)
        print('Valor adicionado com sucesso')
    n = str(input('Deseja conitnuar [S/N]: ')).lower()[0]
print(lista)