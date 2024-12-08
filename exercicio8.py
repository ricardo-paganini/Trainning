date = input('Digite uma data (dd/mm/aaa): ')

if len(date) == 10 and date[2] == '/' and date[5] == '/':
    day = int(date[0:2])
    month = int(date[3:5])
    year = int(date[6:10])

    if (1 <= day <= 31) and 1 <= (month <= 12) and (1 <= year <= 9999):
        print('Data válida no formato dd/mm/aaa.')
    else:
        print('Data invalida no formato dd/mm/aaa.')
else:
    print('O texto não corresponde a uma data.')

