'''
2 Stworzyć następujące klasy:
 Library (klasa opisująca bibliotekę), posiadająca pola:
     city
     street
     zip_code
     open_hours (str)
     phone

Employee (klasa opisująca pracownika biblioteki), posiadająca pola:
     first_name
     last_name
     hire_date
     birth_date
     city
     street
     zip_code
     phone

Book (klasa opisująca książkę), posiadająca pola
     library
     publication_date
     author_name
     author_surname
     number_of_pages

Order (klasa opisująca zamówienie), posiadająca pola:
    employee
    student
    books (lista obiektów klasy Book)
    order_date

Dodatkowo:
* Każda klasa ma mieć zaimplementowaną metodę __str__ , która będzie opisywała
obiekt oraz ewentualne obiekty znajdujące się w tym obiekcie
    (np. obiekt Library w obiekcie Book).
* Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas
    tworzenia instancji klasy za pośrednictwem konstruktora.
 * Stworzyć 2 biblioteki 2 instancje klasy), 5 książek, 3 pracowników,
    3 studentów, oraz 2 zamówienia.
 * Wyświetlić oba zamówienia ( print )
'''


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f'Biblioteka w {self.city}, {self.street} {self.zip_code}, '
                f'tel. {self.phone}, godziny otwarcia: {self.open_hours}')


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city,
                 street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f'Pracownik {self.first_name} {self.last_name}, '
                f'ur. {self.birth_date}, '
                f'zatrudniony {self.hire_date}, '
                f'{self.city}, {self.street} {self.zip_code}, '
                f'tel. {self.phone}')


class Book:
    def __init__(self, library, publication_date, author_name, author_surname,
                 number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f'Książka {self.author_name} {self.author_surname}, '
                f'wydana {self.publication_date}, {self.number_of_pages} '
                f'stron, biblioteka: {self.library}')


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        order_header = (f'Zamówienie złożone przez {self.employee} '
                        f'dla {self.student} w dniu {self.order_date} '
                        f'na książki: \n')
        order_books = ''
        for book in self.books:
            order_books = (order_books + book.__str__() + '\n')
        return order_header + order_books


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Student {self.name} {self.surname}'


# Stworzenie instancji klas
l1 = Library('Warszawa', 'Marszałkowska 1', '00-000', '8-20', '123456789')
l2 = Library('Kraków', 'Rynek 1', '11-111', '9-21', '987654321')

e1 = Employee('Jerzy', 'Bibliotekarz', '01.01.2000', '01.01.1970', 'Warszawa',
              'Marszałkowska 1', '00-000', '123456789')
e2 = Employee('Joanna', 'Bibliotekarka', '01.01.2001', '01.01.1971', 'Kraków',
              'Rynek 1', '11-111', '987654321')
e3 = Employee('Piotr', 'Booksiński', '01.01.2002', '01.01.1972', 'Gdańsk',
              'Długa 1', '22-222', '111222333')

b1 = Book(l1, '01.01.2020', 'Adam', 'Mickiewicz', 300)
b2 = Book(l2, '01.02.2021', 'Juliusz', 'Słowacki', 350)
b3 = Book(l1, '01.03.2022', 'Henryk', 'Sienkiewicz', 400)
b4 = Book(l2, '01.04.2023', 'Stefan', 'Żeromski', 450)
b5 = Book(l2, '01.04.2024', 'Bolesław', 'Prus', 500)

s1 = Student('Jan', 'Kowalski')
s2 = Student('Anna', 'Nowak')

o1 = Order(e1, s1, [b1, b2], '15.04.2024')
o2 = Order(e2, s2, [b3, b4, b5], '16.04.2024')

# Wyświetlenie zamówień
print(' ### Lista zamówień na książki ### \n')
print(o1)
print('\n')
print(o2)
