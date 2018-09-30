import random
liczba = random.randint(1, 10)
#print('Wylosowana liczba: ', liczba)

odp = input('Jaka liczbe od 1 do 49 wylosowano: ')

if liczba == int(odp):
    print('Hura !!!!')
else:
    print('No niestety')