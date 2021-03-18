import spotipy as sp

from spotipy.oauth2 import SpotifyOAuth

Sp = sp.Spotify(auth_manager=SpotifyOAuth(client_id="5d6ba60172a84bf2966d5a073b3c02d1",
                                               client_secret="c898a8f530f5478bb5420ec418326421",
                                               redirect_uri="https://spotifycharts.com/regional/global/weekly/latest",#"http://localhost:9000",
                                               scope="user-library-read"))

results = Sp.current_user_playlists()
print(results)
for thing in results.get("items"):
    print(f"playlist: {thing.get('name')} with tracks: {thing.get('tracks')}")