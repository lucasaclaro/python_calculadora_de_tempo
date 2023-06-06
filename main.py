# 1 minuto -> 60 segundos
# 1 hora -> 3.600 segundos
# 1 dia -> 86.400 segundos
# 1 semana -> 604.800 segundos

print('Calculadora de tempo\n')

segundos = int(input('Qual é o total de segundos?:  '))
saldo = segundos

semana = 0
dia = 0
hora = 0
minuto = 0
segundo = 0

print('----' * 20)
print(f'Analisando o valor digitado, {segundos} segundos correspondem a um total de: ')
print('----' * 20)


while True:
    if saldo >= 604800:
        semana = int(saldo / 604800)
        saldo = saldo - (semana * 604800)
        if saldo == 0:
            break
    elif saldo >= 86400:
        dia = int(saldo / 86400)
        saldo = saldo - (dia * 86400)
        if saldo == 0:
            break
    elif saldo >= 3600:
        hora = int(saldo / 3600)
        saldo = saldo - (hora * 3600)
        if saldo == 0:
            break
    elif saldo >= 60:
        minuto = int(saldo / 60)
        saldo = saldo - (minuto * 60)
        if saldo == 0:
            break
    elif saldo >= 1:
        segundo = int(saldo / 1)
        saldo = saldo - (segundo * 1)
        if saldo == 0:
            break


print(f'Semana(s): {semana}.')
print(f'Dia(s): {dia}.')
print(f'Hora(s): {hora}.')
print(f'Minuto(s): {minuto}.')
print(f'Segundo(s): {segundo}.')

print('----' * 20)
print('\nEncerrando o programa...')
