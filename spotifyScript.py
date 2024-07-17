import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = 'playlist-modify-public'
username = your_username
SPOTIPY_CLIENT_ID= your_client_id
SPOTIPY_CLIENT_SECRET= your_client_secret
SPOTIPY_REDIRECT_URI= your_redirect_uri


token = SpotifyOAuth(scope=scope, username=username, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)
spotifyObject = spotipy.Spotify(auth_manager = token)

#create playlist
playlist_name = input("Enter a playlist name: ")
playlist_description = input("Enter a playlist description: ")

spotifyObject.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)

user_input = input('Enter a song: ')
list_of_songs = []

while user_input != 'quit':
    result = spotifyObject.search(q=user_input)
    #print(json.dumps(result, sort_keys=4, indent=4))
    list_of_songs.append(result['tracks']['items'][0]['uri'])
    user_input = input('Enter a song: ')

#find new playlist
prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

#add songs
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=list_of_songs)
