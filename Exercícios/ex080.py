n = 0
lista = list()
for c in range(0, 4):
    var = int(input('Digite um valor: '))
    if c == 0 or var > lista[-1]:
        lista.append(var)
        print('Foi adicionado na ultima posição')
    else:
        pos = 0
        while pos < len(lista):
            if var <= lista[pos]:
                lista.insert(pos, var)
                print(f'O valor foi adicionado na posição {pos}')
                break
            pos += 1
print('#'*60)
print(f'Os valores digitados são: {lista}')