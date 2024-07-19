from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import pprint

#accept date as input from user
date=input("ENTER THE YEAR WHOSE TOP 100 SONGS YOU WISH TO CREATE A PLAYLIST OF (YYYY-MM-DD): ")
year=date.split("-")[0]

#getting top 100 songs
response=requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
response.raise_for_status

webpage=response.text

soup=BeautifulSoup(webpage, 'html.parser')

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

#authorisation using spotipy
SPOTIFY_CLIENT_ID="YOUR_SPOTIFY_CLIENT_ID"
SPOTIFY_CLIENT_SECRET="YOUR_SPOTIFY_CLIENT_SECRET"
SCOPE= "playlist-modify-private"
USERNAME="YOUR_SPOTIFY_USERNAME"

spot = spotipy.Spotify(auth_manager=SpotifyOAuth( 
        scope=SCOPE,
        redirect_uri="https://example.com/",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="YOUR_CACHE_PATH",
        username=USERNAME
    )
)

user_id = spot.current_user()["id"]

#list of song uri's(uniform resource identifier)
song_uris=[]

for song in song_names:
    result = spot.search(q=f"track:{song} year:{year}", type="track") # result returns a json file with track details, artist details and more.

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        
#creating playlist
PLAYLIST_NAME=f"{date} Billboard 100"

new_playlist=spot.user_playlist_create(user=user_id,name=PLAYLIST_NAME,public=False)
print("NEW PLAYLIST CREATED")

#adding to playlist
spot.playlist_add_items(playlist_id=new_playlist["id"],items=song_uris)       
