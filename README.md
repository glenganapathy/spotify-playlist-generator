# Billboard Top 100 Spotify Playlist Creator

This Python script creates a Spotify playlist of the top 100 songs from the Billboard Hot 100 chart for a specified date. It scrapes song data from the Billboard website and uses the Spotify API to generate a playlist.

## Features

- Scrapes Billboard Hot 100 chart for a given date
- Creates a Spotify playlist with the top 100 songs
- Handles Spotify authentication via OAuth

## Requirements

- Python 3.x
- `spotipy` library
- `requests` library
- `beautifulsoup4` library

## Configuration

Update the following variables in the script with your Spotify credentials:

```python
SPOTIFY_CLIENT_ID = "your_spotify_client_id"
SPOTIFY_CLIENT_SECRET = "your_spotify_client_secret"
USERNAME = "your_spotify_username"
cache_path="YOUR_CACHE_PATH"
```

##### Worked on this as part of a module project from Dr. Angela Yu's course on Udemy titled: 100 Days of Code: The Complete Python Pro Bootcamp 
