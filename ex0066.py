num = 0
cont = 0
soma = 0
while True :
    num = int(input('Dgite um numero [dig 999 para parar] :'))
    if num == 999:
        break
    cont += 1
    soma += num
print('ACABOU !!')
print(f'vc digitou {cont} a soma entre eles foi {soma}.')