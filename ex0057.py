sexo = str(input('Digite seu sexo [F / M]: ')).strip().upper()[0]
while sexo not in 'M F':
    sexo = str(input('dados invalidos , informe seu sexo :')).strip().upper()[0]
print('sexo {} registrado com sucesso '.format(sexo))