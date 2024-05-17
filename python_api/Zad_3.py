'''
 . Endpoint, który zwraca listę filmów w postaci obiektów json.
 Kroki do wykonania:
 - pobrać dane z pliku
 - stworzyć klasę Movie (posłuży jako model danych)
 - przeiterować pętlą po wierszach z pliku i stworzyć tyle obiektów klasy Movie ile wierszy
 - wykorzystać metodę magiczną __dict__ do serializacji obiektu
  - zwrócić z metody listę zserializowanych obiektów

    . Endpoint z filmami przenieść pod adres /movies
    . Dodać nowe modele dla reszty danych (links, ratings, tags)
    . Stworzyć pozostałe endpointy dla reszty plików, czyli:
        /links
         /ratings
         /tags
'''

import string
from flask import request, jsonify, Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Movie:
    def __dict__(self):
        return {
            'movieId': self.movieId,
            'title': self.title,
            'genres': [self.genres]
        }

    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres


class Link:
    def __dict__(self):
        return {
            'movieId': self.movieId,
            'imdbId': self.imdbId,
            'tmdbId': self.tmdbId
        }

    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


class Rating:
    def __dict__(self):
        return {
            'userId': self.userId,
            'movieId': self.movieId,
            'rating': self.rating,
            'timestamp': self.timestamp
        }

    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp


class Tag:
    def __dict__(self):
        return {
            'userId': self.userId,
            'movieId': self.movieId,
            'tag': self.tag,
            'timestamp': self.timestamp
        }

    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp

class Movies(Resource):
    def get(self):
        movies = []
        with open('database/movies.csv', 'r', encoding="utf8") as file:
            for line in file.readlines():
                if line == 'movieId,title,genres\n' or line.count(',') > 2:
                    continue # pomijamy pierwszą linię z nagłówkami oraz linie z błędami (więcej niż 2 przecinki)
                movieId, title, genres = line.strip().split(',')
                genres = genres.replace('|', '", "')
                m = Movie(movieId, title, genres)
                movies.append(m.__dict__())
            return jsonify(movies)


class Links(Resource):
    def get(self):
        links = []
        with open('database/links.csv', 'r', encoding="utf8") as file:
            for line in file.readlines():
                if line == 'movieId,imdbId,tmdbId\n' or line.count(',') > 2:
                    continue # pomijamy pierwszą linię z nagłówkami oraz linie z błędami (więcej niż 3 przecinki)
                movieId, imdbId, tmdbId = line.strip().split(',')
                l = Link(movieId, imdbId, tmdbId)
                links.append(l.__dict__())
            return jsonify(links)


class Tags(Resource):
    def get(self):
        tags = []
        with open('database/tags.csv', 'r', encoding="utf8") as file:
            for line in file.readlines():
                if line == 'userId,movieId,tag,timestamp\n' or line.count(',') > 3:
                    continue
                userId, movieId, tag, timestamp = line.strip().split(',')
                t = Tag(userId, movieId, tag, timestamp)
                tags.append(t.__dict__())
            return jsonify(tags)


class Ratings(Resource):
    def get(self):
        ratings = []
        with open('database/ratings.csv', 'r', encoding="utf8") as file:
            for line in file.readlines():
                if line == 'userId,movieId,rating,timestamp\n' or line.count(',') > 3:
                    continue # pomijamy pierwszą linię z nagłówkami oraz linie z błędami (więcej niż 3 przecinki)
                userId, movieId, rating, timestamp = line.strip().split(',')
                r = Rating(userId, movieId, rating, timestamp)
                ratings.append(r.__dict__())
            return jsonify(ratings)


api.add_resource(Movies, '/movies')
api.add_resource(Links, '/links')
api.add_resource(Ratings, '/ratings')
api.add_resource(Tags, '/tags')


if __name__ == '__main__':
    app.run(debug=True)

