import spotipy
from spotipy.oauth2 import SpotifyOAuth
import configparser
from enum import Enum
from musixmatch import Musixmatch


class Game_emotion(Enum):
    Happy = 1
    Sad = 0


config = configparser.ConfigParser()
config.read('variables.cfg')


scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.get('DEFAULT', 'SPOTIPY_CLIENT_ID'), client_secret=config.get(
    'DEFAULT', 'SPOTIPY_CLIENT_SECRET'), redirect_uri=config.get('DEFAULT', 'SPOTIPY_REDIRECT_URI'), scope=scope))

# print(sp.recommendation_genre_seeds())  # Possible genres

'''
The genres I think are most promising:
['acoustic', 'alternative', 'ambient', 'blues', 'children', 'chill', 'classical', 'disney', 'guitar', 'happy', 'jazz', 'movies',
    'piano', 'rainy-day', 'road-trip', 'rock',  'show-tunes', 'singer-songwriter', 'sleep', 'songwriter', 'soundtracks', 'study']
'''

# https://developer.spotify.com/documentation/web-api/reference/#/operations/get-recommendations
# https://spotipy.readthedocs.io/en/2.19.0/?highlight=recommendation#spotipy.client.Spotify.recommendation_genre_seeds

recommended_tracks = sp.recommendations(country="NE",
                                        seed_genres=[
                                            'acoustic', 'movies', 'alternative', 'ambient', 'rainy-day'],
                                        limit=1,
                                        max_danceability=1,
                                        max_energy=1,
                                        max_instrumentalness=1,
                                        min_liveness=0,
                                        max_loudness=1,
                                        target_mode=Game_emotion.Happy.value,
                                        max_speechiness=0.66,
                                        max_tempo=120,
                                        target_valance=Game_emotion.Happy.value,
                                        max_acousticness=0.1)

musixmatch = Musixmatch(config.get('DEFAULT', 'MUSIXMATCH_API_KEY'))

for track in recommended_tracks["tracks"]:
    artists = []
    for artist in track["artists"]:
        artists.append(artist["name"])
    print("Name: "+track["name"], "Artist:", artists, "Id: "+track["id"])
    musixmatch_info = musixmatch.track_search(q_track=track["name"], q_artist=artists[0],
                                              page_size=10, page=1, s_track_rating='desc')

    # Isssue is the first song always right? Only 30% of the lyrics is returned
    song_id = musixmatch_info["message"]["body"]["track_list"][0]["track"]["track_id"]

    print(musixmatch.track_lyrics_get(song_id))

    # print(musixmatch["body"]["track_list"][0]["track"]["track_id"])
