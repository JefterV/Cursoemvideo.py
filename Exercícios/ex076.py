lista = ('Pizza', 40,
         'Esfirra', 3.40,
         'Banana', 4,
         'Agua', 3,
         'Refrigerante', 5)
print('-#'*30)
print(f'{"LISTAGEM DE PREÇOS":^60}')
print('-#'*30)

for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', end= '')
    else:
        print(f'R${lista[item]:>10}')