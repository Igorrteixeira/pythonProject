print('--'*15)
print('CADASTRE UMA PESSOA:')
print('--'*15)
homens = mulher = maior = menor = 0
while True:
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo [ M / F ]:')).upper().strip()[0]
    print('--'*15)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ? [S / N ]')).upper().strip()[0]
    print('--'*15)
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 18:
        menor += 1
    if continuar == 'N':
        break
print(f'No total foram {maior} maior de idade')
print(f'Ao todo temos {homens} homens cadastrado')
print(f'E temos {menor} mulher menor de 18 anos')
