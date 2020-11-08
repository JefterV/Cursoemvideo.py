print('#'*30)
print(f'{"BANCO Santander":^30}')
print('#'*30)
print('')
print('Bem-Vindo ao banco Santander!')
menu = print('| [ 1 ] Para sacar |'
             ' [ 2 ] Para depositar |'
             ' [ 3 ] para outras opções |')
opção = int(input('Sua opção: '))
print('')
cedula = 50
cedula20 = 20
cedula10 = 10
cedula1  = 1
u_ced50 = 0
u_ced20 = 0
u_ced10 = 0
u_ced1  = 0
if opção == 1:
    valor = int(input('Digite o valor: '))
    total = valor
    while True:
        if total >= 50:
            total = total - cedula
            u_ced50 += 1
        else:
            if total >= 20:
                total = total - cedula20
                u_ced20 += 1
            elif total >= 10:
                total = total - cedula10
                u_ced10 += 1
            elif total >= 1:
                total = total - cedula1
                u_ced1 += 1
            if total == 0:
                break

    print(f'Você vai receber {u_ced50} de R$ 50')
    print(f'Você vai receber {u_ced20} de R$ 20')
    print(f'Você vai receber {u_ced10} de R$ 10')
    print(f'Você vai receber {u_ced1} de R$ 1')

elif opção == 2:
    contas = 'Ana Maria'
    senhas = '909090'
    n = 's'
    while n == 's':
        valor = float(input('Digite o valor: '))
        if valor <= 99:
            print('NÃO FOI POSSIVEL CONCLUIR O PEDIDO \n Tente novamente.')
        elif valor >= 100:
            while True:
                conta = str(input('Digite o nome da pessoa completo: ')).strip()
                senha = str(input('Digite a senha: ')).strip()
                if conta == contas and senha == senhas:
                    print('Seu deposito foi concluido com SUCESSO.')
                    n = 'n'
                    break
                else:
                    print('Tente novamente.',end= ' ')

elif opção == 3:
    print('ESTAMOS TRABALHANDO NESSA OPÇÃO')