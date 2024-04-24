# Zad. 2. Dla osób posiadających podstawową wiedzę o pythonie:
'''
d. Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
(rekomendowane wykorzystanie funkcji range ), a następnie wyświetli co
drugi element.
Wykonane zadania należy umieścić w repozytorium na gałęzi python_basic
Każde zadanie należy rozbijać na osobne pliki lub jeśli ktoś potrzebuje to na
osobne katalogi z zachowaniem nazewnictwa zad_1 , zad_2 ... zad_n .
'''

print("Zadanie 2d.")


def codrugielement(listaLiczb):
    listaLiczbC2 = []
    for i in range(len(listaLiczb)):
        if i % 2 == 0:
            continue
        listaLiczbC2.append(listaLiczb[i])
    return listaLiczbC2


listaliczb = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Lista liczb:")
print(listaliczb)

print("Lista co drugiego elementu:")
print(codrugielement(listaliczb))
