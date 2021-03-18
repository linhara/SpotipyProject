import spotipy as sp

from spotipy.oauth2 import SpotifyOAuth
OAuth = SpotifyOAuth(client_id="de445576e2884c55be39229d878d7ca1",
                                               client_secret="66e060d86a3e4f78bdd4e8a65886d3fe",
                                               redirect_uri="http://basicbitch",#"http://localhost:9000",
                                               scope="user-library-read")
Sp = sp.Spotify(auth_manager=OAuth)
token = OAuth.get_cached_token()

playlists = Sp.current_user_playlists()
print(playlists)

for playlist in playlists.get("items"):
    albumTrackList = Sp.playlist(playlist.get('id')).get('tracks').get('items')
    print(f"album: {Sp.playlist(playlist.get('id')).get('name')}")
    for track in albumTrackList:
        if track.get('track') != None:
            print(track.get('track').get('name'))

