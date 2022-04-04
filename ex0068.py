import random
print('=-='*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-='*15)
while True:
    jogador = int(input('Digite um numero :'))
    computador = random.randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'IP':
        v = 0
        tipo = str(input('par ou impar ? [P/I] :')).upper().strip()
    print(f'voce jogou {jogador} eu joguei {computador}. total = {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('vc venceu')
            v += 1
        else:
            print('vc perdeu')
            break
    elif tipo == 'I' :
        if total % 2 == 1:
            print('vc venceu')
            v += 1
        else:
            print('vc perdeu')
            break
    print('Vamos jogar novamente..')
print(f'GAME OVER !vc ganhou {v} vezes .')
