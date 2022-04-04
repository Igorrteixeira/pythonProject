continuar = 'S'
soma = media = quant = maior = menor = 0
while continuar == 'S':
    numero = int(input('Digite um numero :'))
    continuar = str(input('Deseja continuar ? [S/N]')).strip().upper()
    soma += numero
    quant += 1
    media = soma / quant
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print('Vc digitou {} numeros a media entre eles foi {.:2f}'.format(quant, media))
print('O maior valor foi {} e o menor {}'.format(maior, menor))