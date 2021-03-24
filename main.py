import spotipy as sp


def main():
    #username = input("Please enter username: ")
    username = "optige"

    Sp = authenticate(username)

    averagePop = getAveragePop(Sp)
    userPop = getUserPop(Sp, username)

    if (averagePop / 2) < userPop:
        print("You are a basic bitch...")
    else:
        print("Congratulations! You are not a basic bitch!")


def authenticate(username):

    OAuth = sp.oauth2.SpotifyPKCE(
        client_id="de445576e2884c55be39229d878d7ca1",
        username=username,
        redirect_uri="http://localhost:9000",
        scope="user-library-read",
    )
    return sp.Spotify(auth_manager=OAuth)


def getAveragePop(Sp):

    most_played_songs = "https://open.spotify.com/playlist/2YRe7HRKNRvXdJBp9nXFza?code=AQAQZcBQj5p_5ry1PxdeO6oLjBzIkd67MVLfhQul_0HMliIW5k3sx9OEtGWAuswEa94EjUpgZdQEhTYQttclGfHZN6boYLI4zDwu4CERkVpfY0W1FopucXdkhKnV0oPD_-kuv4yKrHI9VkhTSH_XuN5NPiBD8roa9pp_Eclw1I1mE_td9OH_urKanteQtvI8P6d_ZSiueUnRgJ17oZsjqNlLAVHlFxhb1CGlv57fKg"

    popularity_list = []
    for i in range(6):
        popularity_list += [song["track"]["popularity"] for song in Sp.playlist_items(most_played_songs, offset=100 * i).get("items")]

    return sum(popularity_list)/len(popularity_list)


def getUserPop(Sp, user_name):
    userPlaylists = Sp.current_user_playlists().get("items")

    usersPopularity = 0
    songCount = 0
    for playlist in userPlaylists:
        if playlist.get("owner").get("id") == user_name:
            go = True
            j = 0
            currId = playlist.get("id")
            while go:
                songList = Sp.playlist_items(currId, offset=j * 100).get("items")
                for song in songList:
                    if song.get("track"):
                        songCount += 1
                        usersPopularity += song.get("track").get("popularity")
                if len(songList) < 100:
                    go = False
                else:
                    j += 1
    userAveragePop = usersPopularity / songCount
    print(f"Your popularity score is: {userAveragePop}")
    return userAveragePop


if __name__ == "__main__":
    main()


# Ta bort oanvända importer
# Två blankrader efter importer
# Formattering över lag
