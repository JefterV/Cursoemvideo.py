num = int(input('Digite um numero: '))
print ('''Escolha uma opção
[ 1 ] converter para BINARIO
[ 2 ] converter para HEXADECIMAL
[ 3 ] converter para OCTAL''')
op = int(input('QUAL SUA OPÇÃO?'))
if op == 1:
    print('O numero {} convertido para BINARIO é {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('O numero {} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
elif op == 3:
    print ('O numero {} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
else:
    print('\033[31mOPÇÃO INVALIDA.\033[m tente novamente')