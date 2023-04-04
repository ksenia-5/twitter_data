""" 
https://towardsdatascience.com/an-extensive-guide-to-collecting-tweets-from-twitter-api-v2-for-academic-research-using-python-3-518fcb71df2a
https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent
"""

import requests
import os
import json
import datetime
import time

# Get path to user keys and bearer token
cdir = os.getcwd() # current directory
pdir = os.path.dirname(cdir) # parent directory
fpath = os.path.join(pdir,"twitter_creds.json") #add path of parent direcotry to system

# read json file with user keys and bearer token
with open(fpath) as user_file:
    creds = json.load(user_file)
BEARER_TOEKN = creds['BEARER_TOKEN']
TOKENS = [None]
def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(max_results, my_query, next_token): 
    search_url = "https://api.twitter.com/2/tweets/search/recent" 
    query_params = {'query': my_query,
                    'max_results': max_results,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id,attachments.media_keys',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,attachments,entities,referenced_tweets,reply_settings,source',
                    "media.fields":"duration_ms,height,media_key,preview_image_url,public_metrics,type,url,width",
                    'user.fields': 'id,name,username,entities,url,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': next_token}
    return (search_url, query_params)

def connect_to_endpoint(url, headers, params):
    global TOKENS
    params['next_token'] = TOKENS[-1]   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    response = response.json()
    try:
        TOKENS.append(response['meta']['next_token'])
    except:
        pass
    print("next token",TOKENS[-1])
    return response

headers = create_headers(BEARER_TOEKN)
start_time = "2023-03-25T21:00:00.000Z"
end_time = "2023-04-01T19:30:00.000Z"
max_results = 100
it = 0
start = 0

my_query = "tofu"

def get_tweets(next_token):
    url = create_url(max_results, my_query, next_token)
    json_response = connect_to_endpoint(url[0], headers, url[1])
    # print(json_response['data'][0]['created_at'])

    with open(f'data/data_{my_query}_{datetime.datetime.utcnow()}.json', 'w') as f:
        json.dump(json_response, f)

get_tweets(TOKENS[-1])
while TOKENS[-1]:
    if len(TOKENS) > 1 and (TOKENS[-1] == TOKENS[-2]):
        break
    else:
        time.sleep(1)
        get_tweets(TOKENS[-1])
    
