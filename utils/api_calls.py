import requests

def get_movie_by_id(id):
    data = requests.get(f"https://imdb-api.com/fa/API/Title/k_qs8woiv3/{id}/Trailer,Images")
    return data.json()