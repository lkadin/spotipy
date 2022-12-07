import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep
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
        scope="user-library-read user-read-playback-state user-read-recently-played user-modify-playback-state",
    )
)

scope = "user-read-playback-state,user-modify-playback-state"

# Shows playing devices
res = sp.devices()
pprint(res)

# Change track
sp.start_playback(uris=["spotify:track:6gdLoMygLsgktydTQ71b15"])

# Change volume
sp.volume(100)
sleep(2)
sp.volume(50)
sleep(2)
sp.volume(100)
