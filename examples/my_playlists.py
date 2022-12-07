# Shows a user's playlists

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv(".env")

scope = "playlist-read-private"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="user-library-read user-read-playback-state user-read-recently-played",
    )
)
results = sp.current_user_playlists(limit=50)
for i, item in enumerate(results["items"]):
    print(f"{i} {item['name']}")
