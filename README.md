# SpotifyAPI

## prerequisite

- python 3
- pip

## How to run

### In this folder:

On macOS and Linux:
`python3 -m venv env`

On Windows:
`py -m venv env`

### Run virtual enviroment

On macOS and Linux:
`source env/bin/activate`

Windows:
`.\env\Scripts\activate`

### Add required packages

`pip install -r requirements.txt`

## Add packages

After pip installing package do:
`pip freeze > requirements.txt`

## To leave virtual the environment

Leaving the virtual environment:
`deactivate`

## Create token for Spotify

- [Create application token for Spotify](https://developer.spotify.com/dashboard/applications)
- Add client id, client secret and redirect URIs found in _EDIT SETTINGS_
- [Create musixmatch api key](https://developer.musixmatch.com/) find it in Dashboard -> Applications -> Default -> View
- Add everything to _variables.cfg_ like this:

```
[DEFAULT]
SPOTIPY_CLIENT_ID = yourId
SPOTIPY_CLIENT_SECRET = yourSecret
SPOTIPY_REDIRECT_URI = yourCallbackURI
MUSIXMATCH_API_KEY = yourMusixmatchKey
```

## To run the tasks

`python spotifyapi.py`
