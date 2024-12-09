weight = float(input('Digite o seu peso: '))
height = float(input('Digite a sua altura: '))

bmi = weight / (height * height)


if bmi < 18.5:
    print(f'Você está abaixo do peso com um IMC de {bmi:.2f}%')
elif bmi >= 18.5 and bmi <= 24.9:
    print(f'Você está com o peso normal com um IMC de {bmi:.2f}%')
elif bmi >= 25 and bmi <= 29.9:
    print(f'Você está com sobrepeso com um IMC de {bmi:.2f}%')
else:
    print(f'Você está com obesidade com um IMC de {bmi:.2f}%')


