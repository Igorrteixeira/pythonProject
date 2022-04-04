numero = ('zero', 'um','dois','trez','quatro','cinco','seis','sete','oito','nove' ,'dez','onze','doze','treze','quatorze','quinze','dezeceis','desecete','dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um numero de 0 a 20 :'))
    if 0 <= num > 20:
        break
    else:
        num = numero[num]
        print(f' o numero que vc digitou e {num}')
num = int(input('valor invalido digite um numero entre 0 e 20 :'))
print(f' o numero que vc digitou e {num}')



