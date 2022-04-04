distancia = float(input('Qual e a distancia da sua viajem ?'))
val1 = distancia*0.50
val2 = distancia*0.45
if distancia < 200:
    print('Vc esta prestes a começar uma viajem de {}km.\n E o valor da passagem sera R${}'.format(distancia,val1))
else:
    print('Vc esta prestes a começar uma viajem de {}km.\n E o valor da passagem sera R${}'.format(distancia,val2))
