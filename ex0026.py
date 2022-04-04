frase = str(input('digite uma palavra :')).upper() .strip()
print('na sua palavra tem : {} vezes a letra a '.format(frase.count('A')))
print(' a preimeira letra A esta na posição {}'.format(frase.find('A')+1))
print('a ultima letra A esta na posição {} '.format(frase.rfind('A')+1))
