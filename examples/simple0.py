from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from dotenv import load_dotenv

load_dotenv(".env")

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.search(q="weezer", limit=20)
for i, t in enumerate(results["tracks"]["items"]):
    print(" ", i, t["name"])
