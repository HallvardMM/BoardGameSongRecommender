import spotipy
from spotipy.oauth2 import SpotifyOAuth
import configparser
config = configparser.ConfigParser()
config.read('variables.cfg')


scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.get('DEFAULT', 'SPOTIPY_CLIENT_ID'), client_secret=config.get(
    'DEFAULT', 'SPOTIPY_CLIENT_SECRET'), redirect_uri=config.get('DEFAULT', 'SPOTIPY_REDIRECT_URI'), scope=scope))


playlists = sp.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" %
              (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
