while True:
    num = int(input('digite um numero para ver tabuada :'))
    if num < 0 :
        break
    print('-==-'*10)
    for n in range(1, 11):
            print(f'{num} x {n} = {num}')
print('FIM')
