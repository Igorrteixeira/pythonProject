soma = 0
cont = 0
for c in range(1,7):
    num = int(input('digite um numero: '))
    if num % 2 == 0:
        soma += num
print('A soma dos numeros pares e {}'.format(soma))