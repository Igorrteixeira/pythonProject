from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano do seu nascimento :'))
idade = nasc - atual
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))
if idade == 18:
    print('se aliste imediatamnte !!')
elif idade < 18 :
    saldo = 18 - idade
    devia = atual - saldo
    print('Ainda faltam {} seu alistamento sera em {} '.format(saldo,devia))
elif idade > 18:
    saldo  = 18 - idade
    devia = atual + saldo
    print('ja faz {} anos que deveria ter se alistado em :{}'.format(saldo,devia))