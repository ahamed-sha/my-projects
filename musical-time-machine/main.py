import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import pprint

pp = pprint.PrettyPrinter(indent=4)

CLIENT_ID = "313"
CLIENT_SECRET = "313"
REDIRECT_URI = "http://wow.com"
SCOPE = "playlist-modify-private"


# ------------------- GET USER_ID ------------------- #

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]


# ------------------- GET BILLBOARD TOP 100 ------------------- #

user_date = input("Which year would you like to travel? (YYYY-MM-DD):  ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_date}")
content = response.text

soup = BeautifulSoup(content, "html.parser")
songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

song_names_list = []
for song in songs:
    song_name = song.getText()
    song_names_list.append(song_name)


# ------------------- SEARCH AND ADD SONGS TO SPOTIFY PLAYLIST ------------------- #

year = user_date.split("-")[0]
song_uris = []

for song in song_names_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't found!")

playlist_id = sp.user_playlist_create(
    user=user_id,
    name=f"{user_date} Billboard 100",
    public=False,
    description=f"These are the top songs from {year}"
)

playlist_id = playlist_id["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
