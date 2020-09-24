# Check the rate limits remaining on the twitter API.

import tweepy
import yaml

# Get keys
with open("keys.yaml", "r") as file:
    keys = yaml.load(file, Loader = yaml.SafeLoader)

auth = tweepy.OAuthHandler(keys['twitter']['api_key'], keys['twitter']['api_secret_key'])
auth.set_access_token(keys['twitter']['access_token'], keys['twitter']['access_token_secret'])

# Construct the API instance
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

print("/friends/list:", api.rate_limit_status()["resources"]["friends"]["/friends/list"])
print("/followers/list:", api.rate_limit_status()["resources"]["followers"]["/followers/list"])