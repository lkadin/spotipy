import spotipy
from pprint import pprint
from dotenv import load_dotenv

load_dotenv(".env")


def main():
    spotify = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth())
    me = spotify.me()
    pprint(me)


if __name__ == "__main__":
    main()
