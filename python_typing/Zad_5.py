'''
5. Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi
typu int . Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z
parametru pierwszego zawiera taką wartość jaką przekazano w parametrze
drugim.
'''


def sprawdz(l1: list, l2: int) -> bool:
    if l2 in l1:
        return True
    else:
        return False


l1 = [1, 4, 5, 7, 8]
l2 = 3

print(sprawdz(l1, l2))

l2 = 5

print(sprawdz(l1, l2))
