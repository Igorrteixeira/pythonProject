n1 = int(input('primeiro valor :'))
n2 = int(input('segundo valor :'))
n3 = int(input('terceiro valor : '))
menor = n1
maior = n2
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n3 > n2 and n3 > n1:
    maior = n3
print("o menor numero é : {}\n o maior numero é : {} ".format(menor,maior))
