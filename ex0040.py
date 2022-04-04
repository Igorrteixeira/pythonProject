nota1 = float(input('Digite a primeira nota :'))
nota2 = float(input('digite a segunda nota :'))
nota3 = (nota1 + nota2) /2
media = 5.0
if nota3 > media:
    print('Parabens sua media foi {} voce foi \33[1;31mAPROVADO !!\33[m'.format(nota3))
else :
    print('Infelizmente sua media foi {} \33[1;33mREPROVADO !!\33[m'.format(nota3))
