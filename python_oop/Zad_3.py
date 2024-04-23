'''
3 Stworzyć następujące klasy:
 Property (klasa opisująca posiadłość/nieruchomość), posiadająca pola:
     area
     rooms (int)
     price
     address

 House (klasa dziedzicząca klasę Property , która opisuje dom), posiadająca pola:
    plot (rozmiar działki, int)

 Flat (klasa dziedzicząca klasę Property , która opisuje mieszkanie), posiadająca pola:
    floor

 Dodatkowo:
 Każda z klas dziedziczących ma mieć zaimplementowaną metodę __str__ , która będzie opisywała obiekt.
 Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas tworzenia instancji klasy za pośrednictwem konstruktora.
 Stworzyć po jednym obiekcie klasy House oraz Flat, a następnie je wyświetlić.
'''

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
    def __str__(self):
        return f'Posiadłość o adresie {self.address}, o powierzchni {self.area} m2, {self.rooms} pokojach, cena: {self.price} PLN'

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot
    def __str__(self):
        return f'Dom pod adresem {self.address}, o powierzchni {self.area} m2, {self.rooms} pokojach, cena: {self.price} PLN, działka: {self.plot} m2'

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor
    def __str__(self):
        return f'Mieszkanie pod adresem {self.address}, o powierzchni {self.area} m2, {self.rooms} pokojach, cena: {self.price} PLN, piętro: {self.floor}'

# Definicja instancji klas

p1 = House(100, 4, 500000, 'ul. Kwiatowa 1, 43-603 Jaworzno', 500)
f1 = Flat(50, 2, 200000, 'ul. Ogrodowa 2/7, 41-400 Mysłowice', 3)

# Wyświetlenie instancji klas

print('')
print('Obiekt klasy House:')
print(p1)
print('')
print('Obiekt klasy Flat:')
print(f1)
