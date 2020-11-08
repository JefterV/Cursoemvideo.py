expr = str(input('Digite sua expressão: '))
paren = []
for c in expr:
    if c == '(':
        paren.append('(')
    elif c == ')':
        if len(paren) > 0:
            paren.pop()
        else:

            break
if len(paren) == 0:
    print('Sua expressão é valida')
else:
    print('Sua expressão não é valida.')