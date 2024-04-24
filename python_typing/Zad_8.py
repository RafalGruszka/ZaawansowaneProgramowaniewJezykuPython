'''
8. Dla chętnych Rozszerzyć skrypt z punktu 7 o przyjmowanie parametru city ,
który może być przekazywany w wierszu poleceń podczas wykonywania (np.
python main.py --city=Berlin ). Należy wykorzystać moduł argparse do
wczytywania przekazywanych parametrów, a w razie przekazania wartości
ograniczyć pobierane browary do miasta, które zostało wskazane.
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

    def __init__(self, id: int, name: str, brewery_type: str, address1: str,
                 address2: str, address3: str, city: str, state_province: str,
                 postal_code: str, country: str, longitude: float,
                 latitude: float, phone: str, website_url: str, state: str,
                 street: str):
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
        return (f"Brewery: {self.name}, Type: {self.brewery_type}, "
                f"Address: {self.address1}, {self.address2}, {self.address3}, "
                f"{self.city}, {self.state_province}, {self.postal_code}, "
                f"{self.country}, Longitude: {self.longitude}, "
                f"Latitude: {self.latitude}, Phone: {self.phone}, "
                f"Website: {self.website_url}, State: {self.state}, "
                f"Street: {self.street}")


#  API endpoint
url = 'https://api.openbrewerydb.org/v1/breweries'

# Request paremeters
city = 'Las Vegas'
range = 20

# Rsulting parameterized url
city.lower()
city.replace(' ', '_')
by_city = f'?by_city={city}'
by_range = f'&per_page={str(range)}'
url = f'https://api.openbrewerydb.org/v1/breweries{by_city}{by_range}'


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
