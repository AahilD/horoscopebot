import tweepy
import logging
import os
from dotenv import load_dotenv

load_dotenv('.env')

# Authenticate to Twitter
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKE_SECRET']
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
