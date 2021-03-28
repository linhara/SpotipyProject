import spotipy as sp
from flask import Flask,request,render_template
app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template('index.html')

@app.route("/app.py")
def main():
    playlist_url ="https://open.spotify.com/playlist/2YRe7HRKNRvXdJBp9nXFza?code=AQAQZcBQj5p_5ry1PxdeO6oLjBzIkd67MVLfhQul_0HMliIW5k3sx9OEtGWAuswEa94EjUpgZdQEhTYQttclGfHZN6boYLI4zDwu4CERkVpfY0W1FopucXdkhKnV0oPD_-kuv4yKrHI9VkhTSH_XuN5NPiBD8roa9pp_Eclw1I1mE_td9OH_urKanteQtvI8P6d_ZSiueUnRgJ17oZsjqNlLAVHlFxhb1CGlv57fKg"

    userName = request.args.get('username')
    Sp = authenticate(userName)

    totalPopSum, nrOfSongs = getListAvgPop(Sp,playlist_url)
    avgPop = totalPopSum/nrOfSongs
    userAvgPop = getUserPop(Sp, userName)
    if (avgPop / 2 < userAvgPop):
        return(f"The average popularity is: {avgPop/2}, Your popularity score is: {userAvgPop}.You are a basic bitch")
    else:
        return(f"The average popularity is: {avgPop/2}, Your popularity score is: {userAvgPop}.Congrtulations! You are not a basic bitch!")


def getListAvgPop(Sp, id):
    popularity_list = []
    j = 0
    while True:
        new_songs = [song["track"]["popularity"] for song in Sp.playlist_items(id, offset=100 * j).get("items") if song['track']]
        if (len(new_songs) == 0): break
        popularity_list += new_songs
        j += 1

    return sum(popularity_list), len(popularity_list)


def getUserPop(Sp, userName):
    userPlaylists = Sp.current_user_playlists().get("items")
    total_popularity = 0
    total_length = 0
    for playlist in userPlaylists:
        popSum, playlistLen = getListAvgPop(Sp, playlist.get("id")) if (
                playlist.get("owner").get("id") == userName) else (0, 0)

        total_popularity += popSum
        total_length += playlistLen

    return total_popularity / total_length


def authenticate(userName):
        OAuth = sp.oauth2.SpotifyPKCE(client_id="de445576e2884c55be39229d878d7ca1",
                                      username=userName,
                                      redirect_uri="http://localhost:9000",
                                      scope="user-library-read")

        return sp.Spotify(auth_manager=OAuth)

if __name__ == '__main__':
    #app.run(host = '0.0.0.0',debug=False)
    app.run(debug=False)


