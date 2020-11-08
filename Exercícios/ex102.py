def fatorial(num, show=False):
    '''
    -> Calcula Fatorial de um numero.
    :param num: Indica qual numero irá ser calculada a fatorial
    :param show: indica se irá mostrar o calcula 'False' para não e 'True' para sim.
    :return: retorna o resultado da fatorial
    '''
    contador = 1
    for c in range(num, 0, -1):
        contador = contador * c
        if show:
            print(c,end=' ')
            if c > 1:
                print('x',end=' ')
            else:
                print('=', end=' ')
    return contador

print(fatorial(5))
help(fatorial)