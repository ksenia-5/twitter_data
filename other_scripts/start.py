import os
import sys 
import requests
from tweepy import API, OAuthHandler, Stream
import time
import pandas as pd
import json


cdir = os.getcwd() # current directory
pdir = os.path.dirname(cdir) # parent directory
fpath = os.path.join(pdir,"twitter_creds.json") #add path of parent direcotry to system

# convert creds to json file?
with open(fpath) as user_file:
    creds = json.load(user_file)

# print(creds)
API_KEY = creds["API_KEY"]
API_KEY_SECRET = creds["API_KEY_SECRET"]
ACCESS_TOKEN = creds['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = creds['ACCESS_TOKEN_SECRET']

# # SListener inherits from Stream class in Tweepy
# class SListener(Stream):
#     def __init__(self, api = None):
#         # open new timestamped file to store tweets, takes optional api argument
#         self.output = open('tweets_%s.json' % time.strftime('%Y%m%d-%H%M%S'), 'w')
#         self.api = api or API()
stream = Stream(
    API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
# # authenticate with twitter, using four tokens
# # consumer key authentication
# auth = OAuthHandler(API_KEY, API_KEY_SECRET)
# # access key authentication
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# # set up the API with the authentication handler
# api = API(auth)

# # Instantiate listener object
# listen = SListener(api)

# # Instantiate stream object
# stream = Stream(auth, listen, access_token = ACCESS_TOKEN, access_token_secret = ACCESS_TOKEN_SECRET)
# # stream.sample()
keywords_to_track = ['#sustainable', '#plastic']

stream.filter(track = keywords_to_track)
