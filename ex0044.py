print(f' \33[1;35m{"LOJAS RODRIGUES":=^40}\33[m')
compra = float(input('valor das compras :'))
print ('''formas de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão ''')
opção = int(input('qual e a sua opção ?'))
if opção == 1:
    valor = compra - (compra*30/100)
    print('sua compra no valor de {} ficou {} à vista com 30% de desconto.'.format(compra,valor))
elif opção == 2:
    valor = compra - (compra*5/100)
    print('sua compra no valor de {} ficou {} no catão à vista com 5% de desconto .'.format(compra,valor))
elif opção == 3:
    print('sua compra no valor de {} em 2x não recebe desconto nem acrecimo .'.format(compra))
elif opção == 4:
    valor = compra + (compra*20/100)
    print('sua compra no valor de {} em 3x fica {} com 20% de juros .'.format(compra,valor))
else:
    print('\33[1;31m***OPÇÃO INVALIDA***')