""" Retomando json com strings"""
import json
from pprint import pprint  # serve pra dar print bonito em dict
from typing import TypedDict


class Movie(TypedDict):  # serve só pra tipagem
    title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characteres: list[str]


str_json = '''
{
    "title": "The Lord of the rings",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characteres": ["Frodo", "Sam"]
}
'''

movie: Movie = json.loads(str_json)  # transforma string em json
pprint(movie)
movie_string = json.dumps(movie, ensure_ascii=False)  # volta p/ string
print(movie_string)
