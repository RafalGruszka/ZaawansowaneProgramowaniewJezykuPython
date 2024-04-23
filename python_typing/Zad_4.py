'''
4. Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma
dwóch pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę
informację jako typ logiczny bool
'''


def sprawdz(l1: int, l2: int, l3: int) -> bool:
    if l1+l2 >= l3:
        return True
    else:
        return False


l1 = 1
l2 = 3
l3 = 5


print(f'Czy {l1} + {l2} >= {l3}?')
print(sprawdz(l1,l2,l3))

l1 = 3
l2 = 4
l3 = 5


print(f'Czy {l1} + {l2} >= {l3}?')
print(sprawdz(l1,l2,l3))
