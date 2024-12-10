
sum_number = 0

counter = 0

number = float(input('Digite um número: '))

while number >= 0:

    sum_number += number

    counter += 1

    number = float(input('Digite outro número: '))

mean = sum_number / counter

print(f'A média dos números digitados foi de: {mean:.2f}')