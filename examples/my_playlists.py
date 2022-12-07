# Shows a user's playlists

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv(".env")
SPOTIPY_CLIENT_ID = os.getenv("client_id")
SPOTIPY_CLIENT_SECRET = os.getenv("client_secret")
SPOTIPY_REDIRECT_URI = os.getenv("redirect_uri")

scope = 'playlist-read-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI,
                                               scope="user-library-read user-read-playback-state user-read-recently-played"))
results = sp.current_user_playlists(limit=50)
for i, item in enumerate(results['items']):
    print(f"{i} {item['name']}")