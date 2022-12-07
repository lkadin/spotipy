# shows artist info for a URN or URL

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv(".env")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth())

response = sp.new_releases()

while response:
    albums = response["albums"]
    for i, item in enumerate(albums["items"]):
        print(albums["offset"] + i, item["name"])

    if albums["next"]:
        response = sp.next(albums)
    else:
        response = None
