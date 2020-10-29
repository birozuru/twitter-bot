#!/usr/bin/env python3
# TWITTWER-BOT/bots/config.py

import tweepy
import logging
import os

logger = logging.getLogger()

# To set your environment variables in your terminal run the following line:
# export CONSUMER_KEY='<your_consumer_key>'
# export CONSUMER_SECRET='<your_consumer_secret>'
# export ACCESS_TOKEN='<your_access_token>'
# export ACCESS_TOKEN_SECRET='<your_access_token_secret>'

def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
