# The `spotipy` Package

The `spotipy` package provides an interface into the Spotify API.

## References

The Spotify API:

  + https://developer.spotify.com/documentation/web-api/
  + https://developer.spotify.com/documentation/general/guides/authorization-guide
  + https://developer.spotify.com/documentation/general/guides/scopes/

The `spotipy` Package:

  + https://github.com/plamere/spotipy
  + https://github.com/plamere/spotipy#quick-start
  + https://spotipy.readthedocs.io/en/latest/
  + https://spotipy.readthedocs.io/en/latest/#client-credentials-flow
  + https://spotipy.readthedocs.io/en/latest/#authorization-code-flow

## Installation

First install the package, if necessary:

```sh
pip install spotipy
```

## Setup

Create a [Spotify API Client application](https://developer.spotify.com/dashboard/applications/), note its credentials (`SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET`).

## Authentication

It is simplest to try one of the following basic authentication methods (depending on whether you are working in Colab or locally). Otherwise if you need a specific user's data, skip down to the "User Authentication" section below.

### Basic Authentication

You can use this approach to directly pass the credentials (for example if using notebook secrets in Colab):

```py
from google.colab import userdata
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

# for example if using notebook secrets:
SPOTIPY_CLIENT_ID = userdata.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = userdata.get("SPOTIPY_CLIENT_SECRET")

creds = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
client = Spotify(client_credentials_manager=creds)
print("CLIENT:", type(client))
```

Otherwise if running locally, we can use environment variables to specify the credentials indirectly instead:

```py
import os
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv() # load environment variables

# for example if using environment variables (spotipy package will check for them implicitly):
#print("CLIENT ID:", os.environ.get("SPOTIPY_CLIENT_ID")) 
#print("CLIENT SECRET:", os.environ.get("SPOTIPY_CLIENT_SECRET"))

# FYI, this client configuration approach expects / implicitly uses env vars named SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET
client_credentials_manager = SpotifyClientCredentials()
client = Spotify(client_credentials_manager=client_credentials_manager)
```

If your app doesn't need to make authenticated requests on behalf of the user, this setup should be sufficient. Feel free to move on to the "Basic Usage" example below.

### User Authentication

However, if your app does need to make authenticated requests on behalf of the user, there are a few more setup steps.

First, in your client application's developer settings, you'll need to specify a redirect URL. If you're not sure which URL to designate, feel free to choose your GitHub repository URL, or a local URL like `http://localhost:5000/auth/spotify/callback`. Store the value in an environment variable called `SPOTIPY_REDIRECT_URL`.

Note your Spotify username, and store in an environment varible called `SPOTIFY_USERNAME`.

After setting the redirect URL and username, setup the code provided in the "Advanced Usage" section below, and invoke the provided `get_token()` function. This process will download a file called `.cache-USERNAME` to the root directory of the repo. It looks like this:

```json
{
    "access_token": "_____",
    "token_type": "Bearer",
    "expires_in": 3600,
    "refresh_token": "______",
    "scope": "playlist-read-private",
    "expires_at": 1554651631
}
```

Since this file contains secret credentials, ignore it from version control by adding an entry like `.cache-*` to your repository's ".gitignore" file (if working locally).

Subsequent requests will use the auth token from this credentials file to avoid additional user logins (see the `get_playlists()` function provided in the "Advanced Usage" section below).

## Usage

### Basic Usage

Example request which doesn't require user authentication (i.e. a song search):

```py
response = client.search(q="Springsteen on Broadway", limit=20)

for i, track in enumerate(response['tracks']['items']):
    print(' ', i, track['name'])
```

### Advanced Usage

Example request which requires authentication (i.e. listing a user's playlists):

```py
# adapted from: https://github.com/s2t2/playlist-service-py/blob/4db80cd3f8f2ed018f64bc2a97629d2af105acc3/app/spotify_service.py

import os
from dotenv import load_dotenv

from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

load_dotenv() # load environment variables

# env vars used implicitly by the spotipy package:
#print("CLIENT ID:", os.environ.get("SPOTIPY_CLIENT_ID")) 
#print("CLIENT SECRET:", os.environ.get("SPOTIPY_CLIENT_SECRET"))
#print("REDIRECT URL:", os.environ.get("SPOTIPY_REDIRECT_URI"))

USERNAME = os.environ.get("SPOTIFY_USERNAME", "OOPS")

# requires user interaction
def get_token():
    AUTH_SCOPE = "playlist-read-private"
    token = util.prompt_for_user_token(USERNAME, AUTH_SCOPE)
    return token

# requires user auth
def get_playlists():
    token = get_token()
    client = Spotify(auth=token)

    response = client.current_user_playlists()

    for i, playlist in enumerate(response['items']):
        print(f"{i + 1 + response['offset']} {playlist['uri']} {playlist['name']}")


if __name__ == "__main__":

    get_playlists()
```
