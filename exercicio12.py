age = input('Digite a sua idade: ')
gender = input('Digite seu gênero: ')

age = int(age)
gender = gender.lower()

if age >= 60 and gender == 'mulher':
    print('Elegível a aposentadoria.')
elif age >=65 and gender == 'homem':
    print('Elegível a aposentadoria')
else:
    print('Não elegível a aposentadoria.')