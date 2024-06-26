'''
 . Przenienieść stworzony endpoint dostępny pod adresem
/test
'''

from flask import request, jsonify, Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/test')

if __name__ == '__main__':
    app.run(debug=True)