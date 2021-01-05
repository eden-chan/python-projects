from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
SPOTIFY_CLIENT_ID = "143c18d64de54c50aa126edee3a553d7"
SPOTIFY_CLIENT_SECRET_ID = "dd609f49a7be4268811990a3e78f44d9"
# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET_ID,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

# #Searching Spotify for songs by title
# song_uris = []
# year = date.split("-")[0]
# for song in song_names:
#     result = sp.search(q=f"track:{song} year:{year}", type="track")
#     # print(result)
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")

# #Creating a new private playlist in Spotify
# playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, description="Web scraped")
# print(playlist)
#
# #Adding songs found into the new playlist
# sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris)

# DELETE PLAYLISTS
my_playlists = sp.current_user_playlists()['items']
pprint(my_playlists)
for playlist in my_playlists:
    if playlist['name'] == "Top Songs from 2002":
        sp.current_user_unfollow_playlist(playlist['id'])
        print(f"removing{playlist['name']}")