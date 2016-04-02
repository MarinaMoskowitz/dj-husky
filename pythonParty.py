

#list all the albums released by that artist
"""
birdy_uri = 'spotify:artist:0EmeFodog0BfCgMzAIvKQp'
spotify = spotipy.Spotify()

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
"""

#add tracks to the playlist
import pprint
import sys

import spotipy
import spotipy.util as util

if len(sys.argv) > 3:
    username = sys.argv[1]
    playlist_id = sys.argv[2]
    track_ids = sys.argv[3]
else:
    print ("Usage: %s username playlist_id track_id ... " % sys.argv[0])

print("one")
scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope)
print("two")
if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
    print (results)
else:
    print ("Can't get token for", username)


# Creates a playlist for a user

import pprint
import sys
import os
import subprocess

import spotipy
import spotipy.util as util


if len(sys.argv) > 2:
    username = sys.argv[1]
    playlist_name = sys.argv[2]
else:
    print("Usage: %s username playlist-name" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlists = sp.user_playlist_create(username, playlist_name)
    pprint.pprint(playlists)
else:
    print("Can't get token for", username)

    

