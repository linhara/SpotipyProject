import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

playlist_url ="https://open.spotify.com/playlist/2YRe7HRKNRvXdJBp9nXFza?code=AQAQZcBQj5p_5ry1PxdeO6oLjBzIkd67MVLfhQul_0HMliIW5k3sx9OEtGWAuswEa94EjUpgZdQEhTYQttclGfHZN6boYLI4zDwu4CERkVpfY0W1FopucXdkhKnV0oPD_-kuv4yKrHI9VkhTSH_XuN5NPiBD8roa9pp_Eclw1I1mE_td9OH_urKanteQtvI8P6d_ZSiueUnRgJ17oZsjqNlLAVHlFxhb1CGlv57fKg"

userName = input("Enter Username: ")
OAuth = sp.oauth2.SpotifyPKCE(client_id="5d6ba60172a84bf2966d5a073b3c02d1",
                                               username= userName,
                                               redirect_uri="http://localhost:9000",
                                               scope="user-library-read")

Sp = sp.Spotify(auth_manager=OAuth)
for i in range(6):
    tracks = Sp.playlist_items(playlist_url, offset = 100 * 1).get('items')
totalPopularity = 0

sumOfSongs = 0
for item in tracks:
    if item.get('track'):
        sumOfSongs +=1
        totalPopularity += item.get("track").get("popularity")

averagePopularity = totalPopularity/sumOfSongs

userPlaylists = Sp.current_user_playlists().get('items')
userProfile   = Sp.user(userName)
print(userProfile)

popularity = 0
for playlist in userPlaylists:

    displayName = Sp.playlist(playlist.get('id')).get('owner').get('display_name')

    print(displayName)
    for item in displayName:
        #if item.get('track'):
        nameOfSongs = item.get('track').get('name')
        popularity += item.get('track').get('popularity')
        print(nameOfSongs)



