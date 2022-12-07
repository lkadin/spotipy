from spotipy.oauth2 import SpotifyOAuth
import spotipy
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv(".env")
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = os.getenv("redirect_uri")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id,
        client_secret,
        redirect_uri,
        scope="user-library-read user-read-playback-state user-read-recently-played",
    )
)

pl_id = "spotify:playlist:5RIbzhG2QqdkaP24iXLnZX"
offset = 0

while True:
    response = sp.playlist_items(
        pl_id, offset=offset, fields="items.track.id,total", additional_types=["track"]
    )

    if len(response["items"]) == 0:
        break

    pprint(response["items"])
    offset = offset + len(response["items"])
    print(offset, "/", response["total"])
