import random
cont = 0
pensou = random.randint(1, 10)
nome = str(input('Digite seu nome :'))
print('ola {} sou seu computador ...\nAcabei de pensar em um numero \nsera que consegue advinhar ?'.format(nome))
palpite = int(input('Qual o seu palpite '))
while palpite is not pensou:
    palpite += int(input('tente mais uma vez :'))
    if pensou < palpite:
        print('MENOS...')
    elif pensou > palpite:
        print('MAIOR...')
print('PARABÉNS VC GANHOU !! o numero e {} você precisou de {} tentativas'.format(palpite,cont))
