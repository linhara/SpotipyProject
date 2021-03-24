import spotipy as sp


def main():
    most_played_songs = "https://open.spotify.com/playlist/2YRe7HRKNRvXdJBp9nXFza?code=AQAQZcBQj5p_5ry1PxdeO6oLjBzIkd67MVLfhQul_0HMliIW5k3sx9OEtGWAuswEa94EjUpgZdQEhTYQttclGfHZN6boYLI4zDwu4CERkVpfY0W1FopucXdkhKnV0oPD_-kuv4yKrHI9VkhTSH_XuN5NPiBD8roa9pp_Eclw1I1mE_td9OH_urKanteQtvI8P6d_ZSiueUnRgJ17oZsjqNlLAVHlFxhb1CGlv57fKg"

    username = input("Please enter username: ")
    Sp = authenticate(username)
    
    averagePop = getListAvgPop(most_played_songs, Sp)
    userPop = getUserPop(username, Sp)
    print(f'Average popularity score: {averagePop / 2}')
    print(f'Your popularity score: {userPop}')

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

def getListAvgPop(id, Sp):  # Creds om ni löser denna med modulo 100 istället.
    popularity_list = []
    j = 0
    while True:
        new_songs = [song["track"]["popularity"] for song in Sp.playlist_items(id, offset=100 * j).get("items")]
        if (len(new_songs) == 0): break
        popularity_list += new_songs
        j += 1

    return sum(popularity_list)/len(popularity_list)

def getUserPop(user_name, Sp):
    userPlaylists = Sp.current_user_playlists().get("items")
    total_popularity = 0
    for playlist in userPlaylists:
        total_popularity += getListAvgPop(playlist.get("id"), Sp) if (playlist.get("owner").get("id") == user_name) else 0

    return total_popularity/len(userPlaylists)

if __name__ == "__main__":
    main()