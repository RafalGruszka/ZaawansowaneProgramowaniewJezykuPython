'''
6. Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu
list . Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć
duplikaty, każdy element podnieść do potęgi 3 stopnia, a następnie zwrócić
powstałą listę.
'''


def combinelists(l1: list[int], l2: list[int]):
    l3 = [x ** 3 for x in l1]
    for i in range(len(l2)):
        if l2[i] not in l1:
            l3.append(l2[i] ** 3)
    return l3


l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]
# oczekiwany wynik to 8 elementów [1,8,27,64,125,216,343,512],
# dwa duplikaty usunięte

print('Lista 1')
print(l1)
print('Lista 2')
print(l2)

print('Lista wynikowa bez duplikatów podniesiona do potęgi 3')
print(combinelists(l1, l2))
