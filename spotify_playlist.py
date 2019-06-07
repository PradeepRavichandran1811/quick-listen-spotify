import spotipy
import sys
import spotipy.util as util
from flask import Flask, render_template, request
from spotipy.oauth2 import SpotifyClientCredentials
app = Flask(__name__)
CLIENT_ID = "94a53da1882a498b827a9053947aa26d"
CLIENT_SECRET = "9e32cd0089e94694b927ebd4de46b940"
art={'charlie puth':'6VuMaDnrHyPL1p4EHjYLi7','imagine dragons':'53XhwfbYqKCa1cC15pYq2q','bruno mars':'0du5cEVh5yTK9QJze8zA0C','shawn mendes':'7n2wHs1TKAczGzO7Dd2rGr','taylor swift':'06HL4z0CvFAxyc27GXpf02','selena gomez':'0C8ZW7ezQVs4URX5aX7Kqx','maroon 5':'0aL7M6qKDacHCtUUch3AhB',
     'dua lipa':'6M2wZ9GZgrQXHCFfjv46we','post malone':'246dkjvS1zLTtiykXe5h60','john mayer':'0hEurMDQu99nJRq8pTxO14','ed sheeran':'6eUKZXaKkcviH0Ku9w2n3V',
     'khalid':'6LuN9FCkKOj5PcnpouEgny','ariana grande':'66CXWjxzNUsdJxJ2JdwvnR','jonas brothers':'7gOdHgIoIKoe4i9Tta6qdD',
     'drake':'3TVXtAsR1Inumwj472S9r4','cardi b':'4kYSro6naA4h99UJvo89HB','justin bieber':'1uNFoZAHBGtllmzznpCI3s','eminem':'7dGJo4pcD2V6oG8kP0tJRR',
     }
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/toptracks",methods=['POST'])
def toptracks():
    urn = 'spotify:artist:'
    if request.method == 'POST':
        artist_ = request.form['name']
        artist_final = artist_.lower()
    artist_id = art[artist_final]
    urn +=artist_id
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    artist = sp.artist(urn)
    # print(artist)
    artist_name = artist['name']
    artist_img = artist['images'][0]['url']

    # print("***************Top 10 Tracks******************")
    top = sp.artist_top_tracks(artist_id, country='US')
    # count = 0
    #print(top)
    i=1
    songs=[]
    audio=[]
    cover=[]
    for track in top['tracks'][:10]:
        print(track)
        songs.append(("Song {}  :".format(i)+" "+track['name'],track['album']['name'],track['uri'],track['album']['images'][0]['url']))
        i+=1
    return render_template("spotify.html", artist=artist_name, artist_img=artist_img ,songs=songs)


if __name__ == "__main__":
    app.run(debug=True)
