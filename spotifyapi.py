import tekore as tk

file = 'tekore.cfg'
conf = tk.config_from_file(file, return_refresh=True)

app_token = tk.request_client_token(
    *conf[:2])

spotify = tk.Spotify(app_token)

album = spotify.album('3RBULTZJ97bvVzZLpxcB0j')
for track in album.tracks.items:
    print(track.track_number, track.name)
