import spotipy
import random
import time
from spotipy.oauth2 import SpotifyOAuth

# important variables

user_id = # TODO: Spotify user id to go here
laptop = # TODO: Spotify laptop device id to go here
# can make other device id variables

rounds_playlists = [
    ('Brittney Made a Rounds Playlist', 'spotify:playlist:74cMK3dTapj9LOLLVdpt14'),
    ('Just Another Rounds Playlist', 'spotify:playlist:6SjoefPMI3jqCIHHICisjg'),
    ('Mostly Stolen from Erin 1hr', 'spotify:playlist:1LzWNrpynPGRyK6vGeNr8V'),
    ('Erin Round 4', 'spotify:playlist:00E2lhBAuoh9KeClY4sJSV'),
    ('Erin Round 6', 'spotify:playlist:4oiQuwhGMXjrYZzmuK2Ma5'),
    ('Erin Round 7', 'spotify:playlist:5Z8VovGPWMmUwg4l7oYB8w')
]

style_playlists = {     # all from Brittney's spotify
    'standard': [
        ('waltz', 'spotify:playlist:3tySq93kdHZO5q9uc0ehH0'),
        ('tango', 'spotify:playlist:0GVhyJpq4fSLeHGc1qzTPT'),
        ('vwaltz', 'spotify:playlist:2x6xsJaLaSRIHtvFBLydFc'),
        ('foxtrot', 'spotify:playlist:5mCQN8F6KdwqCvyDKzgR2k'),
        ('quickstep', 'spotify:playlist:1J2agKYZsWS9ixlz835yxn')
    ],
    'smooth': [
        ('waltz', 'spotify:playlist:5XcRq5MExfvU8CX44Ijzpl'),
        ('tango', 'spotify:playlist:6YNKfwBXcz2zHNX1TiyG9c'),
        ('foxtrot', 'spotify:playlist:4PirFi4xCnNt0XxP23cIuZ'),
        ('vwaltz', 'spotify:playlist:1Zc7QslS7B9t11PmCzFfYn')
    ],
    'latin': [
        ('samba', 'spotify:playlist:5nQulnltzrziO093GNHg9x'),
        ('cha', 'spotify:playlist:6cTchFw9vS6BlXTxWNou1x'),
        ('rumba', 'spotify:playlist:5G159Z30efAsIIwYeIjwjC'),
        ('jive', 'spotify:playlist:3C8sdKT1bZf8g3l8UXCvik')
    ],
    'rhythm': [
        ('cha', 'spotify:playlist:5IW9TKPkrzzaAkIWpY2VJw'),
        ('rumba', 'spotify:playlist:4UPnU85FNSQJhCBFU4X5pz'),
        ('swing', 'spotify:playlist:6IYTGFTZMSOWCuNRb9oECM'),
        ('bolero', 'spotify:playlist:5Punjypn7pBwntjHXcDZFT'),
        ('mambo', 'spotify:playlist:5TTw3HZThOMny3hO9AJGTr')
    ]
}

#setup spotipy
scope = "user-read-playback-state,user-modify-playback-state,playlist-modify-public,user-library-modify,playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

#spotipy functions

def next():
    try:
        sp.next_track()
    except:
        print("next error")

def play():
    try:
        sp.start_playback()
    except:
        print('start playback error')

def pause():
    try:
        sp.pause_playback()
    except:
        print('pause error')

def volume(vol):
    try:
        sp.volume(vol)
    except:
        print('volume error')

def create_playlist(user, pl_name):
    playlist = ''
    try:
        playlist = sp.user_playlist_create(user, pl_name)
    except:
        print('create playlist error')
    return playlist

def get_playlist_songs(dance):
    songs = {}
    try:
        songs = sp.playlist_items(dance)
    except:
        print('error listing playlist songs')
    return songs

def add_songs(playlist_id, songs):
    try:
        sp.user_playlist_add_tracks(user_id, playlist_id, songs)
    except:
        print('error adding tracks')

def delete_playlist(pl_uri):
    try:
        sp.current_user_unfollow_playlist(pl_uri)
    except:
        print('Error deleting playlist')
    return

# rounds functions

#TODO: Implement better
def fadeout():
    for x in range(90, 0, -5):
        volume(x)

def choose_playlist():
    return rounds_playlists[random.randint(0, len(rounds_playlists)-1)]

def get_song(dance):
    tracks = get_playlist_songs(dance)
    index = random.randint(0, len(tracks['items'])-1)
    song = tracks['items'][index]['track']['uri']
    print('got song: ' + song)
    return song

def make_round_playlist(style):
    playlist_name = style
    playlist = create_playlist(user_id, str(style + ' spotipy random'))
    tracks = []
    for dance,id in style_playlists[style]:
        tracks.append(get_song(id))
    add_songs(playlist['uri'], tracks)
    return playlist['uri']

def dance_round(dances, playlist=None):
    volume(100)
    if playlist:
        sp.start_playback(device_id=laptop, context_uri=playlist)
    else:
        next()
        play()
    for i in range(dances):
        print("HERE")
        time.sleep(90) # 25) TESTING
        fadeout()
        pause()
        time.sleep(17) # 10) TESTING
        if i < dances - 1:
            volume(100)
            next()
            play()
    return 1

def play_rounds_from_playlist():
    playlist = choose_playlist()
    print('Starting Standard')
    dance_round(5, playlist[1])
    input('Ready to begin Smooth? ')
    dance_round(4)
    input('Ready to begin Latin? ')
    dance_round(4)
    input('Ready to begin Rhythm? ')
    dance_round(5)


print("Welcome to Spotipy Ballroom Rounds")
create, kind, style = '', '', ''
rounds = []
create = False if input("Should I make a playlist? ")[0] in 'nN' else True
if create:
    num_rounds = int(input('Enter the number of rounds you want: '))

    style = input("What style? ").lower()
    while style not in ['standard', 'smooth', 'rhythm', 'latin']:
        style = input('Enter a legal style name ')
    num_dances = 5 if style in ['standard', 'rhythm'] else 4

    for i in range(num_rounds):
        playlist = make_round_playlist(style)
        dance_round(num_dances, playlist)
        if i < num_rounds-1:
            input('Ready to continue? ')

else:
    play_rounds_from_playlist()
