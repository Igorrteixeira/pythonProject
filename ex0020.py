import random
a1 = str(input('nome :'))
a2 = str(input('nome :'))
a3 = str(input('nome :'))
a4 = str(input('nome :'))
lista = [a1,a2,a3,a4]
sort = random.shuffle(lista)
print('a ordem de apresentação é :')
print(lista)
