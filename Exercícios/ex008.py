n= float (input('Uma distância em metrôs'))
km= n / 1000
hm= n / 100
dam= n / 10
dm= n * 10
cm= n * 100
mm= n * 1000
print ('A medida {}m, equivale a {}km \n{}hm \n{}dam \n{}cm \n{}mm'.format(n, km, hm, dam, dm, cm, mm))