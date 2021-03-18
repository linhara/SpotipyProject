import spotipy as sp

from spotipy.oauth2 import SpotifyOAuth
playlist_url ="https://open.spotify.com/playlist/2YRe7HRKNRvXdJBp9nXFza?code=AQAQZcBQj5p_5ry1PxdeO6oLjBzIkd67MVLfhQul_0HMliIW5k3sx9OEtGWAuswEa94EjUpgZdQEhTYQttclGfHZN6boYLI4zDwu4CERkVpfY0W1FopucXdkhKnV0oPD_-kuv4yKrHI9VkhTSH_XuN5NPiBD8roa9pp_Eclw1I1mE_td9OH_urKanteQtvI8P6d_ZSiueUnRgJ17oZsjqNlLAVHlFxhb1CGlv57fKg"

OAuth = SpotifyOAuth(client_id="5d6ba60172a84bf2966d5a073b3c02d1",
                                               client_secret="c898a8f530f5478bb5420ec418326421",
                                               redirect_uri=playlist_url,
                                               scope="user-library-read")
i = 0
Sp = sp.Spotify(auth_manager=OAuth)
for i in range(6):
    tracks = Sp.playlist_items(playlist_url, offset = 100 * i).get('items')


    for item in tracks:
        if item.get('track'):
            print(item.get('track').get('name'))

