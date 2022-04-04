from time import sleep
print('\33[1;31m==-=='*10)
print('              EMPRESTIMO BANCARIO:')
print('\33[1;31m==-==\33[m'*10)
valor = float(input('Qual e o valor da casa : '))
salario = float(input('Qual e o seu salario : '))
parcelas = float(input('Quantas vezes gostaria de parcelar :'))
print('PROCESSANDO...')
sleep(3)
parc1 = (valor/parcelas)
sal1 = salario * 30/100
if parc1 < sal1:
    print('PARABENS seu emprestimo foi \33[1;31mAPROVADO\33[m a parcela sera no valor de {:.2}'.format(parc1))
else:
    print('{{Seu emprestimo não foi aprovado}} !')