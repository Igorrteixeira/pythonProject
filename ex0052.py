num = int(input('Digite um numero :'))
tot = 0
for c in range(1,num+1):
    if num % c == 0:
        print('\33[1;33m',end='=')
        tot += 1
    else:
        print('\33[1;31m',end='=')
    print('{}'.format(c),end='=')
print('\n\33[m o numero {} foi dividido {} veses'.format(num,tot), end ='')
if tot == 2:
    (print('por isso ele e primo'))
else:
    print(' e por isso ele não e primo')