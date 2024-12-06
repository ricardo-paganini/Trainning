word = input('Digite uma letra: ').lower()

vowels = ('a','e','i','o''u')
          
if word in vowels:
    print(f'A letra {word} é uma vogal.')
else:
    print(f'A letra {word} é uma consoante.')