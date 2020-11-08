import BBC
r1 = float (input('Primeiro segmento: '))
r2 = float (input('Segundo segmento: '))
r3 = float (input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(BBC.azuL,'Os segmentos PODEM formar um triangulo.',BBC.limpa)
else:
    print(BBC.vermelho,'Os segmentos NÃO PODEM formar um triangulo.')