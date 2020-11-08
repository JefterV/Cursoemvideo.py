lista= [ ]
while True:
    var = (int(input('Digite um valor: ')))
    lista.append(var)
    pergunta = str(input('Deseja continuar [S/N]: ')).lower()
    if pergunta == 'n':
        break
print('-'*50)
print(f'Foram digitados {len(lista)} elementos')
print('-'*50)
lista.sort(reverse=True)
print(f'os valores digitados em ordem decrecente: {lista}')
print('-'*50)
if 5 in lista:
    print('O valor 5 foi digitado')
else:
    print('O valor 5, não foi digitado')
print('-'*50)