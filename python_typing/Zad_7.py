'''
7. Dla chętnych Stworzyć skrypt pythonowy, który połączy się z API, które
zawiera informacje o browarach (dokumentacja
https://www.openbrewerydb.org/documentation).
Należy w pythonie zrobić klasę
Brawery , która będzie zawierała takie atrybuty jakich dostarcza API wraz z
odpowiednim typowaniem.
W klasie należy zaimplementować magiczną metodę
__str__ która będzie opisywała dane przechowywane w obiekcie.
Skrypt ma się połączyć do API i pobrać 20 pierwszych obiektów, a następnie
utworzyć listę 20 instancji klasy
Brawery , którą przeiteruje i wyświetli każdy obiekt z osobna.
'''

import requests
import json

class Brewery:
    id: int
    name: str
    brewery_type: str
    address1: str
    address2: str
    address3: str
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: float
    latitude: float
    phone: str
    website_url: str
    state: str
    street: str

    def __init__(self, id: int, name: str, brewery_type: str, address1: str, address2: str, address3: str, city: str, state_province: str, postal_code: str, country: str, longitude: float, latitude: float, phone: str, website_url: str, state: str, street: str):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address1 = address1
        self.address2 = address2
        self.address3 = address3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street
    def __str__(self):
        return f"Brewery: {self.name}, Type: {self.brewery_type}, Address: {self.address1}, {self.address2}, {self.address3}, {self.city}, {self.state_province}, {self.postal_code}, {self.country}, Longitude: {self.longitude}, Latitude: {self.latitude}, Phone: {self.phone}, Website: {self.website_url}, State: {self.state}, Street: {self.street}"

# The API endpoint
url = 'https://api.openbrewerydb.org/v1/breweries'
range = '20'
url = f'https://api.openbrewerydb.org/v1/breweries?per_page={range}'


# A GET request to the API
response = requests.get(url)
print(f'Status odpowiedzi {response.status_code}')

# JSON response
breweries = response.json()

# Parse json to list of Brewery objects
brewery_objects = json.loads(json.dumps(breweries))

# Printing the list of Brewery objects
print('Lista browarów')
for brewery in brewery_objects:
    print(brewery.__str__())



