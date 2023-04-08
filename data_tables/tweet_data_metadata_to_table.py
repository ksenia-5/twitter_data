import pickle
import pandas as pd
import os
from tqdm import tqdm
import json

def build_basic_table(tweets_json, path_to_folder, name):
    tweets_list = []
    # takes tweet_json
    for tweet in tweets_json:
        tweet_obj = json.loads(tweet)

        # Store the user screen name in 'user-screen_name'
        tweet_obj['user-screen_name'] = tweet_obj['user']['screen_name']

        # Check if this is a 140+ character tweet
        if 'extended_tweet' in tweet_obj:
            # Store the extended tweet text in 'extended_tweet-full_text'
            tweet_obj['extended_tweet-full_text'] = tweet_obj['extended_status']['full_text']
        else:
            tweet_obj['extended_tweet-full_text'] = 

        if 'retweeted_status' in tweet_obj:
            # Store the retweet user screen name in 'retweeted_status-user-screen_name'
            tweet_obj['retweeted_status-user-screen_name'] = tweet_obj['retweeted_status']['user']['screen_name']

            # Store the retweet text in 'retweeted_status-text'
            tweet_obj['retweeted_status-text'] = tweet_obj['retweeted_status']['text']
            
        tweets_list.append(tweet_obj)
    return pd.DataFrame(tweets_list)

    basic_table = basic_table[['created_at','author_id', 'conversation_id', 'id', 'lang',
       'edit_history_tweet_ids', 'text', 'reply_settings', 'in_reply_to_user_id','referenced_tweets',
       'entities.mentions', 'public_metrics.retweet_count',
       'public_metrics.reply_count', 'public_metrics.like_count',
       'public_metrics.quote_count', 'public_metrics.impression_count',
       'in_reply_to_user_id', 'entities.annotations', 'entities.hashtags',
       'entities.urls', 'attachments.media_keys']]
    # 'geo.place_id'

    # create a temporary variable
    # that holds created_at info in datetime64 data type
    temp = basic_table['created_at'].astype('datetime64')
    # convert Series to DatetimeIndex
    temp = pd.DatetimeIndex(temp)
    # create new columns to hold the years, months, and days info
    basic_table['year'] = pd.DataFrame(temp.year)
    basic_table['month'] = pd.DataFrame(temp.month)
    basic_table['day'] = pd.DataFrame(temp.day)
    with open(path_to_folder + '/' + name + '_basic_table.pickle', 'wb') as handle:
        pickle.dump(basic_table, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return basic_table

for k in tqdm(os.listdir("tofu_04_04")): # list files in directory
    print(k)
    file_name = os.path.join(os.getcwd(),"tofu_04_04", f"{k}")
    #enter location
    folder = os.path.join(os.getcwd(),"tables")# current directory
    text = folder

    with open(file_name, 'rb') as handle:
        # data = pickle.load(handle)
        tweets_json = handle.read()
        # data = json.loads(data)
        
        print('Building basic table ...')
        basic_table = build_basic_table(tweets_json, path_to_folder= text, name = k)

