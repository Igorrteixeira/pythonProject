from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
     ano = int(input('em que ano {} vc nasceu ? :'.format(pess)))
     idade = atual - ano
     if idade >= 18 :
         totmaior += +1
     else:
         totmenor += +1
print('No total foram {} menores de idade '.format(totmenor))
print('E tambem {} pessoas maiores de idade'.format(totmaior))