numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',  'dezenove', 'vinte')

n = 1
while(n == 1):
    while True:
        pergunta = int(input('Digite um numero de 0 a 20: '))
        if pergunta == range(0, 21):
            break
        print('Tente novamente.', end = ' ')

    print(f'Você digitou o numero {numeros[pergunta]}')
    pergu = int(input('Deseja continuar ou sair? (1/2): ') )
    if pergu == 1:
        n= 1
    elif pergu == 2:
        n = 2
    else:
        op = 3
        while (op == 3):
            print('Está alternativa é incorreta')
            print('Tente novamente.', end=' ')
            pergu = int(input('Deseja continuar ou sair? (1/2): '))
            if pergu == 1:
                n = 1
                op = 1
            elif pergu == 2:
                n = 2
                op = 1


