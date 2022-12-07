# shows artist info for a URN or URL

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
from dotenv import load_dotenv

load_dotenv(".env")

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = "Radiohead"

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
result = sp.search(search_str)
pprint.pprint(result)
