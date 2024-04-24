# Zad. 2. Dla osób posiadających podstawową wiedzę o pythonie:
'''
c. Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
(rekomendowane wykorzystanie funkcji range ), a następnie wyświetli
jedynie parzyste elementy.
'''
print("Zadanie 2 c.")

listaliczb: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista liczb:")
print(listaliczb)


def wyswietlparzyste(listaliczb: list[int]):
    listaliczbparzystych = []
    for i in range(len(listaliczb)):
        if listaliczb[i] % 2 == 0:
            listaliczbparzystych.append(listaliczb[i])
    return listaliczbparzystych


parzyste = wyswietlparzyste(listaliczb)
print('Liczby parzyste:')
print(parzyste)
