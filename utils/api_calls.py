import requests
from django.conf import settings

def get_movie_by_id(id):
    data = requests.get(f"https://imdb-api.com/fa/API/Title/{settings.IMDB_API_KEY}/{id}/Trailer,Images")
    return data.json()