# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vmzJkBTwR1WhU27Fy7XHlU4jWNXFibZD
"""

!pip install tweepy

!pip install TextBlob

import tweepy
import textblob

from textblob import TextBlob

#Authentication  Comsumer Key's

consumer_key = 'S5eNhlPpQ6kZtOB8AWnzZMexi'

consumer_secret = '	HvAekhvUWSYHJfCNkvanjl6uUZXGuPPBdzaPsLB1C1QM0eSusK'

#Authentication Access Token

access_token = '	991715243293364226-RI1d0pG0YcqctWWrMiPrQBWA6SzIMzK'

access_token_secret = 'U8oDp0YeBz7VxS8nbPrB7FtZgdStH6WviltZ3l5YLj41K'

oauth = tweepy.OAuthHandler(consumer_key , consumer_secret)

b = tweepy.OAuthHandler('134' , '213')

oauth.set_access_token(access_token , access_token_secret)

api = tweepy.API(oauth)

public_tweets = api.search('MI')



