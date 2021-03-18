import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

playlist_url ="https://open.spotify.com/playlist/2YRe7HRKNRvXdJBp9nXFza?code=AQAQZcBQj5p_5ry1PxdeO6oLjBzIkd67MVLfhQul_0HMliIW5k3sx9OEtGWAuswEa94EjUpgZdQEhTYQttclGfHZN6boYLI4zDwu4CERkVpfY0W1FopucXdkhKnV0oPD_-kuv4yKrHI9VkhTSH_XuN5NPiBD8roa9pp_Eclw1I1mE_td9OH_urKanteQtvI8P6d_ZSiueUnRgJ17oZsjqNlLAVHlFxhb1CGlv57fKg"

lmao = "http://basicbitch"
OAuth = SpotifyOAuth(client_id="5d6ba60172a84bf2966d5a073b3c02d1",
                                               client_secret="c898a8f530f5478bb5420ec418326421",
                                               redirect_uri="http://basicbitch",
                                               scope="user-library-read")
Sp = sp.Spotify(auth_manager=OAuth)
for i in range(6):
    tracks = Sp.playlist_items(playlist_url, offset = 100 * 1).get('items')
totalPopularity = 0

sumOfSongs = 0
number= tracks[0].get('track').get('popularity')
#print(tracks[0].get('track').get('popularity'))
for item in tracks:
    if item.get('track'):
        sumOfSongs +=1
        #print(f'{item.get("track").get("name")}: {item.get("track").get("popularity")}')
        totalPopularity += item.get("track").get("popularity")

averagePopularity = totalPopularity/sumOfSongs

if number >= averagePopularity:
    print('You are a basic bitch')
else:
    print('You are not a basic bitch')



