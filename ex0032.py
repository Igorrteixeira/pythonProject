ano = int(input('que no quer analizar?'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
     print(' o ano {} e bissesto'.format(ano))
else:
    print ('p ano {} nao e bissesto'.format(ano))
