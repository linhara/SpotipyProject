import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
def main():
    playlist_url ="https://open.spotify.com/playlist/2YRe7HRKNRvXdJBp9nXFza?code=AQAQZcBQj5p_5ry1PxdeO6oLjBzIkd67MVLfhQul_0HMliIW5k3sx9OEtGWAuswEa94EjUpgZdQEhTYQttclGfHZN6boYLI4zDwu4CERkVpfY0W1FopucXdkhKnV0oPD_-kuv4yKrHI9VkhTSH_XuN5NPiBD8roa9pp_Eclw1I1mE_td9OH_urKanteQtvI8P6d_ZSiueUnRgJ17oZsjqNlLAVHlFxhb1CGlv57fKg"

    userName = input("Please enter Username: ")
    OAuth = sp.oauth2.SpotifyPKCE(client_id="5d6ba60172a84bf2966d5a073b3c02d1",
                                               username= userName,
                                               redirect_uri="http://localhost:9000",
                                               scope="user-library-read")

    Sp = sp.Spotify(auth_manager=OAuth)
    if(averagePop(Sp, playlist_url) < userPop(Sp, userName)):
        print('You are a basic bitch...')
    else:
        print('Congratulations! You are not a basic bitch!')
def averagePop (Sp, playlist_url):
    # ----------------------------------------------------------------------------
    # Comparing with a list of more than 500 songs, therefore we go from range 0-6
    # ---------------------------------------------------------------------------
    listOfSongs = []
    for i in range(6):
        listOfSongs.append(Sp.playlist_items(playlist_url, offset = 100 * i).get('items'))
    totalPopularity = 0

    sumOfSongs = 0
    for tracks in listOfSongs:
        for item in tracks:
            if item.get('track'):
                sumOfSongs +=1
                totalPopularity += item.get("track").get("popularity")

            averagePopularity = (totalPopularity/sumOfSongs)/2
    print(f"The average popularity is: {averagePopularity}")
    return averagePopularity

def userPop(Sp, userName):
    userPlaylists = Sp.current_user_playlists().get('items')

    usersPopularity = 0
    songCount = 0
    for playlist in userPlaylists:
        if (playlist.get('owner').get('id') == userName):
            go = True
            j =0
            currId = playlist.get('id')
            while (go):
                songList = Sp.playlist_items(currId, offset=j * 100).get("items")
                for song in songList:
                    if (song.get('track')):
                        songCount += 1
                        usersPopularity += song.get("track").get("popularity")
                if len(songList)<100:
                    go=False
                else:
                    j+=1
    userAveragePop =usersPopularity/songCount
    print(f'Your popularity score is: {userAveragePop}')
    return userAveragePop

if __name__ == '__main__':
    main()