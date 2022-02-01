import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

#Scope and Username Setup
scope = 'playlist-modify-public','playlist-modify-private','user-read-recently-played','playlist-read-private'
username = input("What is your Spotify username? (The original, not your profile name!) ")

#Authorization Flow Setup
token = SpotifyOAuth(scope=scope,username=username)
spotifyObject = spotipy.Spotify(auth_manager = token)

#Creating New Playlist
playlist_name = input("Enter your new playlist name: ")
playlist_description = input("Enter a playlist description: ")

spotifyObject.user_playlist_create(user=username,name=playlist_name,public=False,description=playlist_description)

print(f"\nPlaylist '{playlist_name}' was created successfully.")

#Obtaining Number of Last Played Tracks to Show
num_tracks_to_visualise = int(input("How many tracks would you like to visualise? (Up to 50 tracks only!) "))
list_history = []
list_id_history = []
list_history_viewable = []
history = spotifyObject.current_user_recently_played(limit=num_tracks_to_visualise)

#Obtaining Last Played Tracks
i = 0
while i <= (num_tracks_to_visualise -1) :

	json.dumps(history,sort_keys=4,indent=4)
	
	list_history.append(history['items'][i]['track']['uri'])
	songname_history = history['items'][i]['track']['name']
	artistname_history = history['items'][i]['track']['artists'][0]['name']
	fullname_history = songname_history + " by " + artistname_history
	id_history = history['items'][i]['track']['id']
	list_history_viewable.append(fullname_history)
	list_id_history.append(id_history)
	
	i = i+1

#Printing Last Played Tracks
print("Here are your",num_tracks_to_visualise,"recently streamed tracks.")
for index, track in enumerate(list_history_viewable):
        print(f"{index+1}- {track}")

#Obtaining Seed Tracks
indexes = input("\nEnter a list of up to 5 tracks you'd like to use as seeds. Use indexes separated by a space: ")
indexes = indexes.split()
seed_tracks = [list_id_history[int(index)-1] for index in indexes]

#Obtaining Recommended Tracks
recommendations = spotifyObject.recommendations(limit=50, seed_tracks = seed_tracks)

#Appending Recommended Tracks to Playlist
list_rec = []
list_rec_viewable = []
j = 0
while j <= 49 :
	list_rec.append(recommendations['tracks'][j]['uri'])
	artistname_rec = recommendations['tracks'][j]['artists'][0]['name']
	songname_rec = recommendations['tracks'][j]['name']
	fullname_rec = songname_rec + " by " + artistname_rec
	list_rec_viewable.append(fullname_rec)
	j = j+1

#Showing Recommended Tracks
print("Here are 50 song reccomendations based on your seed tracks.\nThey'll be put into your new playlist immediately.")
for index, track in enumerate(list_rec_viewable):
        print(f"{index+1}- {track}")

#Adding New Playlist To User Library
prePlaylist = spotifyObject.user_playlists(user=username,limit=50, offset=0)
playlist = prePlaylist['items'][0]['id']

#Adding Songs to New Playlist and Finishing
spotifyObject.user_playlist_add_tracks(user=username,playlist_id=playlist,tracks=list_rec)
print(f"\nRecommended tracks successfully uploaded to playlist '{playlist_name}'.\nExiting program...")

quit()