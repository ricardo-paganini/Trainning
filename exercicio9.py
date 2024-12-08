grade1 = input('Digite a 1ª nota: ')
grade2 = input('Digite a 2ª nota: ')
grade3 = input('Digite a 3ª nota: ')

grade1 = float(grade1)
grade2 = float(grade2)
grade3 = float(grade3)

average = (grade1 + grade2 + grade3) / 3

if average >= 6:
    print('APROVADO')
    if average >= 6 and average == 10:
        print('Parabéns ! APROVADO')
else:
    print('REPROVADO')