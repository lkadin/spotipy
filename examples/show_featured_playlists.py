# shows artist info for a URN or URL

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv(".env")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth())

response = sp.featured_playlists()
print(response["message"])

while response:
    playlists = response["playlists"]
    for i, item in enumerate(playlists["items"]):
        print(playlists["offset"] + i, item["name"])

    if playlists["next"]:
        response = sp.next(playlists)
    else:
        response = None
