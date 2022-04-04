num = 0
cont = 0
soma = 0
num = int(input('Dgite um numero [dig 999 para parar] :'))
while num != 999 :
    cont += 1
    soma += num
    num = int(input('Dgite um numero [dig 999 para parar] :'))
print('ACABOU !!')
print('vc digitou {} a soma entre eles foi {}.'.format(cont,soma))