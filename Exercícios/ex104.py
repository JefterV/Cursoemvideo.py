def leia_int(num):
    while True:
        var = input(num)
        if var.isnumeric():
            n = int(var)
            return n
            break
        else:
            print('ERRO. Digite um numero valido.')


n = leia_int('Digite um numero: ')
print(f'Você digitou o valor {n}')