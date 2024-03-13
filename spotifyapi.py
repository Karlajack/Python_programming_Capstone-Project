import requests
import json

# spotify client_id and client_secret generated from creating an app from spotify for developers
CLIENT_ID = '5e8de1f6a4bd4ee3bd513f09b528b788'
CLIENT_SECRET = '88da4a7cdcc449f0ab98b9657e7e7c96'

   
# spotify api url
AUTH_URL = 'https://accounts.spotify.com/api/token'

# function for generating access token for the API
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

# search the artist by their name

def search_for_artist(token,artist_name):
    url="https://api.spotify.com/v1/search"
    headers=get_auth_header(token)
    query=f"?q={artist_name}&type=artist&limit=1"

    query_url=url + query

    response= requests.get( query_url, headers=headers)
    
    response_json = response.json()
   
    results=response_json["artists"]["items"]
# Return the artist if exist else return None
    if len(results) == 0:
        print(f" No artist with {artist_name} exists")
        return None
    else:
        return results[0]

         
        
token = get_token()    
result = search_for_artist(token,"boyz")
artist_name=result["name"]

print(f"artist_name: {artist_name}")

