temperature = input('Digite a temperatura: ')

temperature = float(temperature)

if 36 <= temperature <= 37:
    print('Temperatura está na faixa da normalidade.')
elif temperature < 36:
    print('Temperatura está abaixo da normalidade.')
else:
    print('Temperatura está acima da normalidade.')

 