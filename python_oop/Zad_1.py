'''
 1. Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz
 jedną metodę is_passed, która zwraca wartość logiczną, pozytywną gdy średnia
ocen jest > 50 w przeciwnym przypadku negatywną. Następnie należy
stworzyć 2 przykładowe obiekty klasy, tak aby dla pierwszego obiektu metoda
zwracała true , a dla drugiego false
'''


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return sum(self.marks) / len(self.marks) > 50


s1 = Student('Jan', [50, 60, 70])
s2 = Student('Anna', [40, 30, 20])

print(f'Student {s1.name} is_passed = {s1.is_passed()}')
print(f'Student {s2.name} is_passed = {s2.is_passed()}')
