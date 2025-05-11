""" Retomando json com arquivos """
import json
import os


FILE = 'aula290.json'
FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    FILE
)

movie = {
    'characteres': ['Frodo', 'Sam'],
    'imdb_rating': 8.8,
    'is_movie': True,
    'title': 'The Lord of the rings',
    'year': 2001
}

with open(FILE_PATH, 'w', encoding='utf-8') as file:
    json.dump(movie, file, indent=2)

with open(FILE_PATH, 'r', encoding='utf-8') as file:
    json_movie = json.load(file)
    print(json_movie)
