from flask_restx import Resource, Namespace
from models import GenreSchema, Genre
from setup_db import db

genres_ns = Namespace('genre')
genre_schema = GenreSchema()
genre_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresesView(Resource):
    def get(self):
        all_genres = db.session.query(Genre).all()
        return GenreSchema.dump(all_genres), 200