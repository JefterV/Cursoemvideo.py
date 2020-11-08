n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
if n1 > n2:
    print ('O \033[32mprimeiro\033[m numero é maior')
elif n2 > n1:
    print('O \033[31msegundo\033[m numero é maior')
else:
    print('\033[1;31;40mOs dois numeros tem o mesmo valor.\033[m')