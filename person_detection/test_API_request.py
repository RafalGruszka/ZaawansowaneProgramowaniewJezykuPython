import requests
import cv2 as cv

url = 'https://www.wroclaw.pl/beta2/files/news/100149/maindworzec%20glowny.jpg'
url2 = 'https://th.bing.com/th/id/OIP.XAmpx08xwKo_s7EuNbXDtQHaDH?w=330&h=147&c=7&r=0&o=5&dpr=1.3&pid=1.7'
url3 = 'https://webp-konwerter.infor.pl/eyJmIjoiaHR0cHM6Ly9nOS5pbmZvc/i5wbC9wL19maWxlcy8xNDEwMDAvZm/90b2xpYV81NTQwNzAzOV9zdWJzY3J/pcHRpb25feGwuanBnIiwidyI6NzcxfQ.webp'
host = 'http://127.0.0.1:5000'

endpoint1 = '/countPersonsAPI/v1/'
endpoint2 = '/countPersonsAPI/v2/'
endpoint3 = '/countPersonsAPI/v3/'

##### Przed wywołanie należy uruchomić serwer w pliku API #####

print('Wywołanie endpointu 1 GET: /countPersonsAPI/v1/ - analiza zdjącia z dysku: downloaded_image.jpg')
response1 = requests.get(host + endpoint1)
print(response1.json())

print('Wywołanie endpointu 2 GET: /countPersonsAPI/v2/ - analiza zdjącia z url: downloaded_imageV2.jpg')
response2 = requests.get(host + endpoint2, params={'url': url2})
print(response2.json())

print('Wywołanie endpointu 3 POST: /countPersonsAPI/v3/ - analiza przesłanego zdjącia: downloaded_imageV3.jpg')
response = requests.post(url3)
response.content_type = 'image'

img = response.content # cv.imread('downloaded_imageV3.jpg')
response3 = requests.post(host + endpoint3, data=img)
print(response3.json())

# W zależności od wybranego zdjęcia, wynik może być różny, ale można modyfikować
# wartość zmiennej score w pliku countPersons.py, aby zmienić próg detekcji osoby
# aktualna warość:  score > 0.6