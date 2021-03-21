import spotipy as sp

def main():
    userName = input("Please enter Spotify Username: ")
    OAuth = sp.oauth2.SpotifyPKCE(client_id="de445576e2884c55be39229d878d7ca1",
                                                   username= userName,
                                                   redirect_uri="http://localhost:9000",
                                                   scope="user-library-read")

    Sp = sp.Spotify(auth_manager=OAuth)

    avgPop = avaragePopularity(Sp)
    userAvgPop = userPopularity(Sp,userName)

    if (avgPop / 2 < userAvgPop):
        print(f"You are a basic bitch")
    else:
        print(f"Congrtulations! You are not a basic bitch!")

#---------------------------------------------------
# The playlist we compare popularity against is a little over 500 songs.
# therefore we can loop 6 times to get 5*100 + one last iteration with
# the rest of the songs.
#---------------------------------------------------
def avaragePopularity(Sp):
    playlist_url ="https://open.spotify.com/playlist/2YRe7HRKNRvXdJBp9nXFza?code=AQAQZcBQj5p_5ry1PxdeO6oLjBzIkd67MVLfhQul_0HMliIW5k3sx9OEtGWAuswEa94EjUpgZdQEhTYQttclGfHZN6boYLI4zDwu4CERkVpfY0W1FopucXdkhKnV0oPD_-kuv4yKrHI9VkhTSH_XuN5NPiBD8roa9pp_Eclw1I1mE_td9OH_urKanteQtvI8P6d_ZSiueUnRgJ17oZsjqNlLAVHlFxhb1CGlv57fKg"
    tracksList = []
    for i in range(6):
        tracksList.append(Sp.playlist_items(playlist_url, offset = 100 * i).get('items'))

    totalPopularity = 0
    sumOfSongs = 0

    for tracks in tracksList:
        for item in tracks:
            if item.get('track'):
                sumOfSongs +=1
                totalPopularity += item.get("track").get("popularity")

    averagePopularity = totalPopularity/sumOfSongs
    print(f"The average popularity is: {averagePopularity/2}")
    return averagePopularity


def userPopularity(Sp,userName):
    userPlaylists = Sp.current_user_playlists().get('items')
    usersPopularity = 0
    songCount = 0

    for playlist in userPlaylists:
        if (playlist.get('owner').get('id') == userName):
            go = True
            j = 0
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

