import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

def main():
    #username also necessary to see which playlists are actually yours in future
    uName = input("input Spotify Username: ")
    OAuth = sp.oauth2.SpotifyPKCE(client_id="de445576e2884c55be39229d878d7ca1",
                                                   username = uName,
                                                   redirect_uri="http://localhost:9000",#"http://localhost:9000",
                                                   scope="user-read-private user-library-read",)

    Sp = sp.Spotify(auth_manager=OAuth)


    playlists = Sp.current_user_playlists()
    print(playlists)

    for playlist in playlists.get("items"):
        albumTrackList = Sp.playlist(playlist.get('id')).get('tracks').get('items')

        for track in albumTrackList:
            if track.get('track'):
                print(track.get('track').get('name'))


if __name__ == "__main__":
    main()

