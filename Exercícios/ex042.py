import playsound
r1 = int(input('Segmento um: '))
r2 = int(input('Segmento dois: '))
r3 = int(input('Segmento três: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima, PODEM formar um triangulo', end=' ')
    if r1 == r2 and r2 == r3:
        playsound.playsound('rllx.mp3', tr)
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Os segmentos acima NÃO PODEM formar um triangulo')