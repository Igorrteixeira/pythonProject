maior = menor = total = cont = 0
barato = ' '
primeiro = maior = menor
print('=--='*15)
print('LOJAS ARCANJO MIGUEL')
print('=--='*15)
while True:
    produto = str(input('Nome do produto :'))
    preço = float(input('Preço R$:'))
    total += preço
    cont += 1
    if preço > 1000:
        maior += 1
    if cont == 1:
        menor = preço
        barato = produto
    else :
        if preço < menor:
            menor = preço
            barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ? [ S / N ]')).strip().upper()
    if continuar == 'N':
        break
print(f' o total de compras foi R${total}')
print(f'temos o total de {maior} custando mais de R$1000.00. ')
print(f'O produto {barato} e o mais barato custa {menor}')

