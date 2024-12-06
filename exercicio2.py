number = input('Digite um número: ')

number = float(number)

if number > 0:
    print(f'{number} é positivo.')
elif number < 0:
    print(f'{number} é negativo.')
else:
    print(f'{number} não é nem positivo e nem negativo. ')