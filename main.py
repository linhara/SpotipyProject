import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

def main():
    uName = input("input Spotify Username: ")
    OAuth = sp.oauth2.SpotifyPKCE(client_id="de445576e2884c55be39229d878d7ca1",
                                                   username = uName,
                                                   #username = 'linusharaldsson1',
                                                   redirect_uri="http://localhost:9000",#"http://localhost:9000",
                                                   scope="user-read-private user-library-read",)

    Sp = sp.Spotify(auth_manager=OAuth)


    playlists = Sp.current_user_playlists()
    print(playlists)


    for playlist in playlists.get("items"):
        go = True
        j = 0
        currId = playlist.get('id')
        while (go):
            songList = Sp.playlist_items(currId, offset=j * 100).get("items")
            for song in songList:
                if (song.get('track')):
                    print(song.get('track').get('name'))
            print(f"------LENGTH: {len(songList)}")
            if len(songList)<100:
                go=False
            else:
                j+=1
                #print(songList)
                #for songObj in songList:
                   # print(songObj.get('name'))


if __name__ == "__main__":
    main()

