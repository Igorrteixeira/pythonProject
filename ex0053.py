nome = str(input( 'digite uma frase : ')) .strip().upper()
palavra = nome.strip()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso+= junto[letra]
print(junto,inverso)
if inverso == junto:
    print('temos uma palindromo ')
else:
    print('a frase nao e um palindromo !')