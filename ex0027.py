frase = str(input('digite seu nome completo')).upper().strip()
nome = frase.split()
print('seu primeiro nome é : {}'.format(nome[0]))
print('seu ultimo nome é : {}'.format(nome[len(nome)-1]))
