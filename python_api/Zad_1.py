'''
 1. Stworzyć endpoint, który zwraca respone
{'hello': 'world'} , uruchomić serwer
i sprawdzić w przeglądarce czy endpoint zwraca odpowiednie dane.
'''

from flask import request, jsonify, Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)