# The `tweepy` Package

The `tweepy` package provides some useful tweeting capabilities. :bird: :bird:

Reference:

  + [Package](https://pypi.python.org/pypi/tweepy/3.7.0)
  + [Website](http://www.tweepy.org/)
  + [Source](https://github.com/tweepy/tweepy)
  + [Docs](http://tweepy.readthedocs.io/en/v3.7.0/)
  + [Auth Tutorial](http://tweepy.readthedocs.io/en/v3.7.0/auth_tutorial.html#auth-tutorial)
  + [API Reference](http://tweepy.readthedocs.io/en/v3.7.0/api.html#api-reference)
  + [Status Methods](https://tweepy.readthedocs.io/en/3.7.0/api.html#status-methods)
  + [Pagination](http://tweepy.readthedocs.io/en/v3.7.0/code_snippet.html#pagination)
  + [Twitter Developer Account - Getting Started](https://developer.twitter.com/en/account/get-started)

## Setup

Create a Twitter Account. Then while logged in to Twitter, visit the [Twitter Application Management Console](https://developer.twitter.com/en/apps) and click "Create New App" to create a new Twitter Application. You might have to first sign up for a Twitter developer account, and click the link in a confirmation email.

After creating a new application, click on the "Keys and Access Tokens" tab, and note the application's "Consumer Key" and "Consumer Secret". Scroll down and generate a new Access Token and note its "Access Token" and "Access Token Secret" values. Store these four values in environment variables like the following:

  + `TWITTER_API_KEY`
  + `TWITTER_API_SECRET`
  + `TWITTER_ACCESS_TOKEN`
  + `TWITTER_ACCESS_TOKEN_SECRET`

## Installation

Install `tweepy`, if necessary:

```sh
pip install tweepy
```

## Usage

List your recent tweets:

```py
import os

from dotenv import load_dotenv
import tweepy

load_dotenv()

consumer_key = os.environ.get("TWITTER_API_KEY")
consumer_secret = os.environ.get("TWITTER_API_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

# AUTHENTICATE

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# INITIALIZE API CLIENT

client = tweepy.API(auth)

# ISSUE REQUESTS

user = client.me() # get information about the currently authenticated user

tweets = client.user_timeline() # get a list of tweets posted by the currently authenticated user

# PARSE RESPONSES

print("---------------------------------------------------------------")
print(f"RECENT TWEETS BY @{user.screen_name} ({user.followers_count} FOLLOWERS / {user.friends_count} FOLLOWING):")
print("---------------------------------------------------------------")

for tweet in tweets:
    created_on = tweet.created_at.strftime("%Y-%m-%d")
    print(" + ", tweet.id_str, created_on, tweet.text)
```
