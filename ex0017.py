from math import  hypot
co = float(input('comprimento do cateto oposto :'))
ca = float(input('comprimento do cateto adijacente :'))
hi = hypot(co,ca)
print('a hipotenusa e {:.2f}'.format(hi))
