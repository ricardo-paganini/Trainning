age = input('Digite a sua idade: ')
nationality = input('Digite a sua nacionalidade: ')

if nationality == 'brasileiro':
    nationality = 'brasileira'
    

age = int(age)

if age >= 16 and nationality == 'brasileira':
    print('Você está apto a votar.')
else:
    print('Você não está apto a votar.')