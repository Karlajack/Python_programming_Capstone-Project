import requests

# spotify client_id and client_secret generated from creating an app from spotify for developers

CLIENT_ID = "5e8de1f6a4bd4ee3bd513f09b528b788"
CLIENT_SECRET = "88da4a7cdcc449f0ab98b9657e7e7c96"

   
# spotify api url
AUTH_URL = "https://accounts.spotify.com/api/token"

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

print(get_token())