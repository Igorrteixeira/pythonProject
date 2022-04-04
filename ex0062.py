primeiro = int(input('primeiro temo : '))
razão = int(input('Razão da PA : '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} '.format(termo), end='')
        termo += razão
        c += 1
    print('pausa')
    mais = int(input('Qauntos termos vc quer mostrar a mais ?'))
print('foram mostrados {} termos'.format(total))