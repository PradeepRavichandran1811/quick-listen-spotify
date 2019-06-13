import spotipy
from flask import Flask, render_template, request
from spotipy.oauth2 import SpotifyClientCredentials
app = Flask(__name__)
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/toptracks",methods=['POST'])
def toptracks():
    urn = 'spotify:artist:'
    if request.method == 'POST':
        artist_ = request.form['name']
        artist_final = artist_.lower()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    search=sp.search(artist_final, limit=5, offset=0, type='artist', market=None)
    print(search)
    if search['artists']['items']!=[]:
        artist_id=search['artists']['items'][0]['id']
        urn += artist_id
        artist = sp.artist(urn)
        artist_name = artist['name']
        artist_img = artist['images'][0]['url']
        top = sp.artist_top_tracks(artist_id, country='US')
        i=1
        songs=[]
        for track in top['tracks'][:10]:
            print(track)
            songs.append(("Song {}  :".format(i)+" "+track['name'],track['album']['name'],track['uri'],track['album']['images'][0]['url']))
            i+=1
    else:
        return render_template("error.html")
    return render_template("spotify.html", artist=artist_name, artist_img=artist_img ,songs=songs)


if __name__ == "__main__":
    app.run(debug=True)
