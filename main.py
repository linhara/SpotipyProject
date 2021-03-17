import spotipy as sp

from spotipy.oauth2 import SpotifyOAuth

Sp = sp.Spotify(auth_manager=SpotifyOAuth(client_id="de445576e2884c55be39229d878d7ca1",
                                               client_secret="66e060d86a3e4f78bdd4e8a65886d3fe",
                                               redirect_uri="http://basicbitch",#"http://localhost:9000",
                                               scope="user-library-read"))

results = Sp.current_user_playlists()
print(results)
for thing in results.get("items"):
    print(f"playlist: {thing.get('name')} with tracks: {thing.get('tracks')}")
#for idx, item in enumerate(results['items']):
#    track = item['track']
#    print(idx, track['artists'][0]['name'], " – ", track['name'])