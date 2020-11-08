from datetime import date
informações = { }
informações['nome'] = str(input('Nome: ')).strip().capitalize()
informações['idade'] = int(input('Ano de nascimento: '))
informações['ctps'] = int(input('Carteira de nascimento (0 se não tem): '))
if informações['ctps'] != 0:
    informações['contratação'] = int(input('Ano de contratação: '))
    informações['salario'] = float(input('Salario: '))
print('#='*30)
for k , v in informações.items():
    print(f'{k}: {v}')
if informações['ctps'] != 0:
    print(f'Carteira de trabalho: {informações["ctps"]}')
    data = date.today().year - informações['idade']
    aposento = (informações['contratação'] + 35) - informações['idade']
    print(f'Você tem {data} anos. Vai se formar com {aposento}')
print('#='*30)