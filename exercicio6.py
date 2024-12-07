text = input('Digite um texto ou palavra: ')

if text[::-1] == text:
    print('É um palíndromo.')
else:
    print('Não é palíndrono.')