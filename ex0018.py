import math
angu = float(input(' qual e o seu  angulo ?'))
seno =  math.sin(math.radians(angu))
coseno = math.cos(math.radians(angu))
tang = math.tan(math.radians(angu))
print(' seu seno e : {:.2f} \n seu coseno e : {:.2f}\n sua tangente e : {:.2f}'.format(seno,coseno,tang))
