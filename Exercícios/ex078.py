lista = list()
for p , v in enumerate(range(0, 4)):
    lista.append(int(input(f'Digite um valor para a posição {p}: ')))
    menor = 0
print(f'O menor numero da lista é {min(lista)}, e, apareceu na posição {lista.index(min(lista))+1}')
print(f'O maior é {max(lista)} e apareceu na posição {lista.index(max(lista))+1}')