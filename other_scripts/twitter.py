# !pip3 install tweepy
from tweepy import API, OAuthHandler, OAuth1UserHandler, Stream
import pandas as pd
import json
from utils import flatten_tweets
import os

cdir = os.getcwd() # current directory
pdir = os.path.dirname(cdir) # parent directory
fpath = os.path.join(pdir,"twitter_creds.json") #add path of parent direcotry to system

# convert creds to json file?
with open(fpath) as user_file:
    creds = json.load(user_file)

stream = Stream(consumer_key = creds['API_KEY'],
                consumer_secret = creds['API_KEY_SECRET'], 
                access_token=creds['ACCESS_TOKEN'], 
                access_token_secret=creds['ACCESS_TOKEN_SECRET'])

keywords_to_track = ['#sustainable', '#plastic']

# # SListener inherits from Stream class in Tweepy
# class SListener(Stream):
#     def __init__(self, api = None):
#         # open new timestamped file to store tweets, takes optional api argument
#         self.output = open('tweets_%s.json' % time.strftime('%Y%m%d-%H%M%S'), 'w')
#         self.api = api or API()

# # authenticate with twitter, using four tokens
# # consumer key authentication
# auth = OAuthHandler(consumer_key, consumer_secret)
# # access key authentication
# auth.set_access_token(access_token, access_token_secret)
# # set up the API with the authentication handler
# api = API(auth)

# collect data, using random sample of all twitter data (1%)
# Use the sample endpoint

# # Instantiate listener object
# listen = SListener(api)

# # Instantiate the Stream object
# stream = Stream(auth, listen, access_token, access_token_secret)

# # Call sample method to begin collecting data
# # stream.sample()


# keywords_to_track = ['#sustainable', '#plastic']
# stream.filter(track = keywords_to_track) # Begin collecting data

# # read twitter json
# tweet_json = open('tweet-example.json', 'r').read()
# tweet = json.loads(tweet_json) # convert to python dictionary

# tweet['text'] # tweet text
# tweet['id'] # tweet id
# tweet['user']['screen_name'] # tweet username
# tweet['user']['name'] # user name
# tweet['user']['created_at'] # date user created account
# tweet['user']['description'] # user communty, behaviour, ...
# # Print user follower count
# print(tweet['user']['followers_count'])
# # Print user location
# print(tweet['user']['location'])

# # Print user description
# print(tweet['user']['description'])

# # for tweets > 140 characgers
# print(tweet['extended_tweet']['full_text'])

# # retweets and quoted tweets
# print(tweet['quoted_status']['extended_twee']['full_text'])

# # to create a pandas dataframe with all the tweets
# tweet_list = []
# with open('all_tweets.json', 'r') as fh: # open file full of tweets
#     tweets_json = fh.read().split('\n') 
#     for tweet in tweets_json:
#         tweet_obj = json.loads(tweet)
#         if 'extended_tweet' in tweet_obj:
#             tweet_obj['extended_tweet-full_text'] = tweet_obj['extended_tweet']['full_text']
# tweet_list.append(tweet)
# tweets = pd.DataFrame(tweet_list)
    
    


# # Flatten the tweets and store in `tweets`
# tweets = flatten_tweets(data_science_json)
# # Print out the first 5 tweets from this dataset
# print(ds_tweets['text'].values[0:5])