# +
# Author: 
# Aryan Adhlakha (tweepy tweets extraction part)
# Roxin Liu (tweets formating and saving part)
# -

import tweepy
import unicodedata
import numpy as np
import csv
from textblob import TextBlob
from matplotlib import pyplot as plt
import datetime
import statsmodels.api as sm
from statsmodels.tsa.stattools import grangercausalitytests

# +
consumer_key = 'Ti0pygk3ys8Bq8M5vggUNcnYH'
consumer_secret = 'YCnQGwkbvFuRW4KJmn7VIvyrMJuaxvNglKwNxQR6BQihXzBUde'
access_token = '768348331-Hh7WsjYAf4MiQYkU6jarEqV2UEQEQN72Lkg0WuYx'
access_token_secret = 'tdOl2fZVbK7eW45Ryyulp4MRPUPsTBQ0Qnrc9IZQz9pHe'

filename = 'tweets_mar_dowjones.csv'
begin_date = "2020-03-20" 
end_date = "2020-03-20"
search_terms = "feel OR makes me OR I am OR I'm"
duration = 20 # 20 days of trading and price record

"""
filename = 'tweets_newage.csv'
begin_date = "2020-01-01" 
end_date = "2020-08-31"
search_terms = "feel" or "makes me" or "I am" or "I'm"
"""
# -

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# +
# Open/Create a file to append tweets:
csvFile = open(filename, 'a', newline = '')
csvWriter = csv.writer(csvFile)
#header = ["timestamp", "contents", "user follower count", "polarity", "subjectivity"]
#csvWriter.writerow(header)

print("Ready to extract")
#for tweet in api.search("DJI"):
#for tweet in tweepy.Cursor(api.search, q="dji", since=begin_date, until=end_date).items(3000):
for tweet in tweepy.Cursor(
    api.search, 
    q=search_terms, 
    since=begin_date, 
    until=end_date
    ).items(1000):
    
    analysis=TextBlob(tweet.text)
    timestamp = tweet.created_at.strftime("%Y-%m-%dT%H:%M:%SZ")
    csvWriter.writerow([timestamp, unicodedata.normalize('NFKD', tweet.text).encode('ascii','ignore'), str(tweet.user.followers_count), analysis.sentiment.polarity, analysis.sentiment.subjectivity])

print("Tweets Extraction Done")
csvFile.close()
