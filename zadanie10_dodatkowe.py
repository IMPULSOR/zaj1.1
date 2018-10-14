from random import randint

rozmiar = int(input("Podaj rozmiar macierzy: "))

macierzA = []

for element in range(rozmiar):
    wersA = []
    for liczba in range(rozmiar):
        wersA.append(randint(1,100))
        macierzA.append(wersA)
print(macierzA)

macierzB = []
for element in range(rozmiar):
    wersB = []
    for liczba in range(rozmiar):
        wersB.append(randint(1,100))
        macierzB.append(wersB)
print(macierzB)

macierzC = []
for i in range(rozmiar):
    for j in range(rozmiar):
        macierzC.append(macierzA[i][j]+macierzB[i][j])
print(macierzC)








