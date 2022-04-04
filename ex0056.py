somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = 0
mulhermenos = 0
for p in range(1,5):
    print('-------- {}ªPESSOA ---------'.format(p))
    nome = str(input('qual e o seu nome :'))
    idade = int(input('qual a sua idade :'))
    sexo = str(input('qual seu sexo :(M) ou (F)')).upper().strip()
    somaidade += idade
    if p == 1 and sexo in "Mm ":
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in "Ff" and idade < 20:
        mulhermenos += 1
mediaidade += somaidade / 4
print(' idade media do grupo é {}'.format(mediaidade))
print(' a idade do mais velho é {} e o nome {}'.format(maioridadehomem,nomemaisvelho))
print(' {} sao menores que 20 anos'.format(mulhermenos))