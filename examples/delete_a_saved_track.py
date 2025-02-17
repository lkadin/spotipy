# Delete a track from 'Your Collection' of saved tracks

import pprint
import sys

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-modify"

if len(sys.argv) > 1:
    tid = sys.argv[1]
else:
    print("Usage: %s track-id ..." % (sys.argv[0],))
    sys.exit()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
results = sp.current_user_saved_tracks_delete(tracks=[tid])
pprint.pprint(results)
