def contador(inicio, fim, intervalos):
    if intervalos < 0:
        intervalos *= -1
    if intervalos == 0:
        intervalos = 1
    print(f'De {inicio} até {fim} indo de {intervalos} em {intervalos}')
    cont = inicio
    if inicio <= fim:
        while cont <= fim:
            print(f'{cont}', end=' ')
            cont+= intervalos
    elif inicio >= fim:
        while cont >= fim:
            print(f'{cont}', end=' ')
            cont-= intervalos



comeco = int(input('Começo: '))
final = int(input('Final: '))
pulando = int(input('Intervalos: '))
contador(inicio=comeco, fim=final, intervalos=pulando)
