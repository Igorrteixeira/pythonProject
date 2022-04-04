import random
from time import sleep
from random import randint
lista = ('pedra ','papel','tesoura')
computador = random.randint(0,2)
print('''\33[;1;31mSuas opções:\33[m
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual e a sua jogada'))
sleep(1)
print('**JO')
sleep(1)
print('ken*')
sleep(1)
print('PO**')
print('-==-'*10)
print('O computador jogou {}'.format(lista[computador]))
print('O jogador jogou {}'.format(lista[jogador]))
print('-==-'*10)
if computador == 0 :
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1 :
        print ('JOGADOR VENCE')
    elif jogador == 2 :
        print('COMPUTADOR VENCE')
    else:
        print('jogada invalida')
elif computador == 1 :
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1 :
        print('EMPATE')
    elif jogador == 2 :
        print('JOGADOR VENCE' )
    else:
        print('jogada invalida')
elif computador == 2 :
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1 :
        print('COMPUTADOR VENCE')
    elif jogador == 2 :
        print('EMPATE')
    else:
        print('jogada invalida')
