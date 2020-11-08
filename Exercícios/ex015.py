d = int(input('O carro foi alugado por quantos dias?'))
km = float (input('Ele percorreu quantos KM?'))
din1 = d * 60
din2= km * 0.15
resultado= din1 + din2
print  ('Você alugou o carro por {} dias e percorreu {}km. De acordo com essa informações, você tera que pagar R${:.2f}'.format(d, km, resultado))
print ('')
d1 = int (input('Por quantos dias você alugou o carro?'))
hm1 = float (input ('Quantos km ele percorreu?'))
rs = d1 * 60 + hm1 * 0.15
print ('De acordo com as informações, você nos deve {:.2f}'.format(rs))