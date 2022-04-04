import time
from time import sleep
soma = 0
multiplica = 0
maior = 0
novo = 0
num1 = int(input('Digite primeiro numero :'))
num2 = int(input('Digite segundo numero :'))
opção = 0
while opção != 5 :
    print( '''    [ 1 ] somar :
    [ 2 ] multiplicar :
    [ 3 ] maior nº :
    [ 4 ] novos numeros :
    [ 5 ] sair do programa :''')
    print('-==-'*12)
    opção = int(input('Qual a sua opção ?'))
    print('-==-'*12)
    if opção == 1 :
        soma = num1 + num2
        print('a soma entre {} e {} é : {}'.format(num1,num2,soma))
    elif opção == 2 :
        multiplica = num1 * num2
        print(' a multiplicação entre {} e {} é : {}'.format(num1,num2,multiplica))
    elif opção == 3:
        if num1 > num2:
            maior = num1
        if num2 > num1:
            maior = num2
        print('o maior numero entre {} e {} é :{}'.format(num1,num2,maior))
    elif opção == 4:
        print('digite os numeros novamente :')
        num1 = int(input('Digite primeiro numero :'))
        num2 = int(input('Digite segundo numero :'))
    elif opção == 5:
        print('FIM')
    else :
        print ('opção invalida :')