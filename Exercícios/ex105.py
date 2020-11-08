def nota(*notas, situ=False):
    '''
    -> Recebe as notas de uma sala, guarda em um dicionario e mostra os resultados relevantes.
    :param notas: todas notas
    :param situ: situação(opcional)
    :return: retorna os valores relevantes
    '''
    dic = dict()
    media = sum(notas) / len(notas)
    dic['total'] = len(notas)
    dic['maior'] = max(notas)
    dic['menor'] = min(notas)
    dic['media'] = media
    if situ:
        if media <= 5:
            dic['situação'] = 'Ruim'
        elif media <= 7:
            dic['situação'] = 'Razoavel'
        elif media > 7:
            dic['situação'] = 'Boa'
    print(dic)

#nota(1,3,7,10, situ=True)
help(nota)
