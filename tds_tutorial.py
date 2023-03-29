""" 
https://towardsdatascience.com/an-extensive-guide-to-collecting-tweets-from-twitter-api-v2-for-academic-research-using-python-3-518fcb71df2a
https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent
"""

import requests
import os
import json
import pandas as pd
# import csv
# import datetime
# import dateutil.parser
# import unicodedata
# import time

from tweepy import API, OAuthHandler, OAuth1UserHandler, Stream
# from utils import flatten_tweets

# Get path to user keys and bearer token
cdir = os.getcwd() # current directory
pdir = os.path.dirname(cdir) # parent directory
fpath = os.path.join(pdir,"twitter_creds.json") #add path of parent direcotry to system

# read json file with user keys and bearer token
with open(fpath) as user_file:
    creds = json.load(user_file)
    
# read user credentials
API_KEY = creds["API_KEY"]
API_KEY_SECRET = creds["API_KEY_SECRET"]
ACCESS_TOKEN = creds['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = creds['ACCESS_TOKEN_SECRET']
BEARER_TOEKN = creds['BEARER_TOKEN']

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(keywords, start_date, end_date, max_results = 10):
    
    search_url = "https://api.twitter.com/2/tweets/search/recent" #Change to the endpoint?
    #change params based on the endpoint you are using
    query_params = {'query': keywords,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': {}}
    return (search_url, query_params)

def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

headers = create_headers(BEARER_TOEKN)
keywords = ["sustainability goals"]
start_time = "2023-03-23T00:00:00.000Z"
end_time = "2023-03-29T00:00:00.000Z"
max_results = 10


url = create_url(keywords, start_time, end_time, max_results)
# url = create_url(keyword, max_results)
json_response = connect_to_endpoint(url[0], headers, url[1])
print(json.dumps(json_response, indent=4, sort_keys=True))
json_response['data'][0]['created_at']

with open('data1.json', 'w') as f:
    json.dump(json_response, f)