import pandas as pd
import numpy as np
from utils import flatten_tweets

data_science_json = None #json file from twitter

# Flatten the tweets and store them
flat_tweets = flatten_tweets(data_science_json)

# Convert to DataFrame
ds_tweets = pd.DataFrame(flat_tweets)

# Find mentions of #python in 'text'
python = ds_tweets['text'].str.contains('#python', case = False)

# Print proportion of tweets mentioning #python
print("Proportion of #python tweets:", np.sum(python) /python.shape[0] )


def check_word_in_tweet(word, data):
    """Checks if a word is in a Twitter dataset's text. 
    Checks text and extended tweet (140+ character tweets) for tweets,
    retweets and quoted tweets.
    Returns a logical pandas Series.
    """
    contains_column = data['text'].str.contains(word, case = False)
    contains_column |= data['extended_tweet-full_text'].str.contains(word, case = False)
    contains_column |= data['quoted_status-text'].str.contains(word, case = False)
    contains_column |= data['quoted_status-extended_tweet-full_text'].str.contains(word, case = False)
    contains_column |= data['retweeted_status-text'].str.contains(word, case = False)
    contains_column |= data['retweeted_status-extended_tweet-full_text'].str.contains(word, case=False)
    return contains_column

# Find mentions of #python in all text fields
python = check_word_in_tweet('#python', ds_tweets)

# Find mentions of #rstats in all text fields
rstats = check_word_in_tweet('#rstats', ds_tweets)

# Print proportion of tweets mentioning #python
print("Proportion of #python tweets:", np.sum(python) / python.shape[0])

# Print proportion of tweets mentioning #rstats
print("Proportion of #rstats tweets:", np.sum(rstats) / python.shape[0])