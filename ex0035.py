print('-==-'*15)
print( 'ANALIZANDO O TRIANGULO')
print('-==-'*15)
n1 = float(input('primeiro segmento :'))
n2 = float(input('segundo segmento :'))
n3 = float(input('terceiro segmento :'))
if n2 + n3 > n1 and n1 + n2 > n3 and n1 + n3 > n2:
    print('Analizando as medidas PODE FORMAR UM TRIANGULO')
else:
    print('Analizando as medias NAO PODEM FORMAR UM TRIANGULO')
