import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="b7bf94e8355a41499f343af52b879860",
                                               client_secret="2520477e8835405888556dc271691fad",
                                               redirect_uri="http://kadinenterprises.com/",
                                               scope="user-library-read user-read-playback-state user-read-recently-played"))

# Shows playing devices
res = sp.devices()
pprint(res)

# Change track
sp.start_playback(uris=['spotify:track:6gdLoMygLsgktydTQ71b15'])

# Change volume
sp.volume(100)
sleep(2)
sp.volume(50)
sleep(2)
sp.volume(100)
