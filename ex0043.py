peso = float(input('Qual e o seu peso : (kg)'))
altura = float(input('Qual e a sua altura: (M) '))
imc = peso/ altura**2
print('Seu IMC e :{:.1f}'.format(imc))
if imc <= 18.5:
    print('Você esta abaixo do peso :')
elif 18.5 <= imc < 24.9:
    print('Seu peso esta normal')
elif 24.9 <= imc < 29.9:
    print('Você esta acima do peso :')
elif 29.9 <= imc < 34.9:
    print('OBESIDADE NIVEL 1')
elif 34.9 <= imc < 39.9:
    print('OBESIDADE NIVEL 2 (SEVERA):')
else:
    print('OBESIDADE NIVEL 3 (MORBIDA):')