"""
This python programming capstone project search Top songs/tracks from spotify by artist_name
"""

import requests
import json

# spotify client_id and client_secret generated from creating an app from spotify for developers
CLIENT_ID = '5e8de1f6a4bd4ee3bd513f09b528b788'
CLIENT_SECRET = '88da4a7cdcc449f0ab98b9657e7e7c96'



   
# spotify api url
AUTH_URL = 'https://accounts.spotify.com/api/token'

# function for posting credentials to spotify to generate access token for the API
def get_token():
    auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    })
    auth_response_data = auth_response.json()
    token = auth_response_data['access_token']
    return token

#function for header authorization 

def get_auth_header(token):
    return {"Authorization":"Bearer "+token}

# Searching the favorite artist by name

def search_for_artist(token,artist_name):
    url="https://api.spotify.com/v1/search"
    headers=get_auth_header(token)
    query=f"?q={artist_name}&type=artist&limit=1"

    query_url=url + query

    response= requests.get( query_url, headers=headers)
    
    response_json = response.json()
   
    results=response_json["artists"]["items"]

    if len(results) == 0:
        print(f" No artist with {artist_name} exists")
        return None
    else:
        return results[0]


# Getting the top tracks from spotify for the artist
def get_tracks_by_artist(token,artist_id):

    url= f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=KE"
    headers=get_auth_header(token)
    response= requests.get(url, headers=headers)
    response_json = response.json()
    results=response_json["tracks"]
    return results

         
token = get_token()    
result = result = search_for_artist(token,input("Search artist name: "))

artist_id = result["id"]
artist_name=result["name"]
tracks= get_tracks_by_artist(token,artist_id)

# printing top songs in spotify for the artist
print("-------------------------------------")
print (f"Top tracks by: {result["name"]}")
print("-------------------------------------")
for index,track in enumerate(tracks):
        print (f"{index+1}.{track["name"]}")









