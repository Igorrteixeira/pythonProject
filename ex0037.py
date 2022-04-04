num = int(input('Digite um numero :'))
print( '''Escolha uma das bases para conversão :
[ 1 ] BINARIO
[ 2 ] OCTA
[ 3 ] HEXADECIMAL''')
op = int(input('Sua opção :'))
if op == 1:
    print('{} convertido para BINARIO e igual a {}'.format(num,bin(num)[2:]))
elif op == 2 :
    print('{} convertido para OCTA  e igual a {}'.format(num,oct(num)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL e igual a {}'.format(num,hex(num)[2:]))
else :
    print('Opção invalidade :')