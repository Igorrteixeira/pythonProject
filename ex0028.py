import random
from time import sleep
resp = random.randint(0,5)
print('-==-'*15)
print (' VOU PENSAR EM UM NUMERO ENTRE 0 E 5 TENTE ADIVINHAR...')
print('-==-'*15)
numero = int(input('Em que numero eu estou pensando ?'))
print('PROCESSANDO...')
sleep(3)
if resp:
    print ('PARABENS! VOCÊ VENCEU !')
else:
    print('GANHEI Eu pensei no numero {} e nao no numero {} !'.format(resp, numero))
