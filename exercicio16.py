a = float(input('Digite 1º número: '))
b = float(input('Digite 2º número: '))
operation = input('Digite a operação desejada (+,-,*,/): ')

result = 0

match operation:
    case '+':
        result = (a + b)
        print(f'O resultado da soma entre {a} + {b} = {result:.2f}')
    case '-':
        result = (a - b)
        print(f'O resultado da subtração entre {a} - {b} = {result:.2f}')
    case '*':
        result = (a * b)
        print(f'O resultado da multiplicação entre {a} * {b} = {result:.2f}')
    case '/':
        result = (a / b)
        print(f'O resultado da divisão entre {a} / {b} = {result:.2f}')
    case _:
        print('Você não digitou a operação corretamente.')