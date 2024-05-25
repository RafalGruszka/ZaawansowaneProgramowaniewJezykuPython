'''
Projekt - liczenie osób na zdjęciu
'''


from flask import request, jsonify, Flask
from flask_restful import Api, Resource
import cv2 as cv
import countPersons as cp
import requests


app = Flask(__name__)
api = Api(app)


'''
 3  API posiada 1 endpoint GET, który odczytuje zdjęcie z dysku i zwraca 
liczbę osób.
'''

# Endpoint 1 -  endpoint GET, który odczytuje zdjęcie z dysku i zwraca liczbę osób
class CountPersons(Resource):
    def get(self):

        img = cv.imread('downloaded_image.jpg')
        nop = cp.countPersons(img)
        return {'number_of_persons': nop}


api.add_resource(CountPersons, '/countPersonsAPI/v1/')

# Endpoint 2 - CountPersonsfromURL
#  endpoint GET, który przyjmuje url do # zdjęcia znajdującego się w Internecie,
#  endpoint zwraca liczbę osób na tym zdjęciu

class CountPersonsfromURL(Resource):
    def get(self):

        url = request.args.get('url')
        response = requests.get(url)
        response.raise_for_status()

        with open('downloaded_imageV2.jpg', 'wb') as f:
            f.write(response.content)

        img = cv.imread('downloaded_imageV2.jpg')
        nop = cp.countPersons(img)

        return {'number_of_persons': nop}


api.add_resource(CountPersonsfromURL, '/countPersonsAPI/v2/')


# Endpoint 3 - endpoint POST, do którego można przesłać zdjęcie
class CountPersonsFromPicture(Resource):
    def post(self):

        requests.content_type = 'image/jpeg'
        img = request.data
        print(type(img))
        with open('downloaded_imageV3.jpg', 'wb') as fl:
            fl.write(img)

        img = cv.imread('downloaded_imageV3.jpg')
        nop = cp.countPersons(img)

        return {'number_of_persons': nop}


api.add_resource(CountPersonsFromPicture, '/countPersonsAPI/v3/')

# Uruchomienie serwera
if __name__ == '__main__':
    app.run(debug=True)
