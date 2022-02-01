# Smart Spotify Playlists
Ever wanted something MORE than your Discover Weekly on Spotify? 

A playlist that not only lets you select songs to base your new tracks in, BUT ALSO immediately enters your library without having to click a single button on the Spotify app itself? 

Here it is folks, all yours - just read these few notes before you begin!

*Clarification: I wrote and ran this code on a MacOS command line, so just be aware when setting up libraries or environment variables to run commands compatible to YOUR system!

### Install the Right Libraries
This short piece of code uses the Python3 language, as well as the JSON and Spotipy Python3 libraries. 
Spotipy is specifically designed for accessing Spotify's Web API, allowing you to gain full access to all music data on the platform. 
Install the necessary Python packages by running: 
`pip3 install -r requirements.txt` and `pip3 install spotipy --upgrade` on your terminal.

### Set Up a Spotify for Developers Application
To start, set up an account at [Spotify for Developers](https://developer.spotify.com/dashboard/), and create an application. This will give you get the credentials necessary to make authorized calls - a client id and client secret. These will be 2 of 3 environment variables to be exported.

This code uses the [Authorization Code Flow](https://spotipy.readthedocs.io/en/2.19.0/#authorization-code-flow) for the Spotipy library. [This link](https://spotipy.readthedocs.io/en/2.19.0/#redirect-uri) tells you how to set up your redirect URI, the last of your environment variables. 

### Run the Code
Export the environment variables which you set up before:

```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'

export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'

export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
```

Finally, run the entry-point script and follow the console instructions:

`python3 smartspotifyplaylists.py`

That's it! Have fun with this small code! Thanks for using it!

<div align="right">Sincerely,

Youngseo Park</div>
