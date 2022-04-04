salario = float(input('Qual e o seu salario ?'))
salario1 = salario * 10/100
salario2 = salario * 15/100
if salario > 1250:
    print ('voce ganhava R${} seu aumento e 10% passa a receber R${}'.format(salario,salario+salario1))
if salario < 1250:
    print ('voce ganhava R${} seu aumento é 15% passa a receber R${}'.format(salario,salario+salario2))
