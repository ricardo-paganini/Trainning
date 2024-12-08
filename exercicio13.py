dividend = input('Digite o 1º número inteiro: ')
divider = input('Digite o 2º número inteiro: ')

dividend = int(dividend)
divider = int(divider)


result = dividend / divider
rest = dividend % divider

if result.is_integer() == True and rest == 0:
    print(f'{dividend} e {divider} são divisíveis.')
else:
    print(f'{dividend} e {divider} não são divisíveis.')
