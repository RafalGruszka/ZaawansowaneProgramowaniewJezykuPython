# Zad. 2. Dla osób posiadających podstawową wiedzę o pythonie:
'''
# a. Utwórz funkcję, która otrzyma w parametrze listę 5 imion, a następnie
#wyświetli każde z nich.
'''

print("Zadanie 2a.")

imiona = ["Jan", "Marek", "Rafał", "Zbyszek","Robert"]

def wyswietl_imiona(names):
    for imie in names:
        print(imie)

wyswietl_imiona(imiona)


