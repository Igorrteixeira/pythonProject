from datetime import date
ano = int(input('Digite um ano : '))
atual = date.today().year
idade = atual - ano
print('atleta tem {} anos .'.format(idade))
if idade <= 9:
    print('CLASSIFICAÇÃO : MIRIN')
elif idade >= 10 and  idade <= 14:
    print('CLASSIFICAÇÃO : INFANTIL')
elif idade >= 15 and idade <= 19:
    print('CLASSIFICAÇÃO : JUNIOR')
elif idade >= 20 and idade == 25 :
    print('CLASSIFICAÇÃO : SÊNIOR ')
else:
    print('CLASSIFICAÇÃO : MASTER')

