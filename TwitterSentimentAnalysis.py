import tweepy
from textblob import TextBlob

consumer_key="h2B4revL8MCycfohwdLEM90Tl"
consumer_secret="bgR1tqwSR4ij8ig5GyHJPxiAL1LPhNdQezO2q2onlz8OaftZit"
access_token="1144563824986451968-muUGnzwnMUBoWgioSgqDTl5b4r8OQx"
access_token_secret="KwTKtU85G7lTVBdFsoet4efNzR8K64AhHtLa2o7j1m33h"

auth=tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token , access_token_secret)

api= tweepy.API(auth)
public_tweets= api.search('MumbaiFloods')

for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
