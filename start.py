#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 01:34:07 2018

@author: abha
"""

import re
import tweepy
from tweepy import OAuthHandler
#from textblob import TextBlob
from sentiment_mod import Initialize
import sentiment_mod
from flask import Flask, request, jsonify

app = Flask(__name__)

 
class TwitterClient(object):
    
    def __init__(self):
        
        consumer_key = 'ML1OP1Oxe81AZjXrp6UYHXb14'
        consumer_secret = 'eEeOyMuzsi7TkAtmo1tFXrAusNLBxVYQClYw9DP4DNe5RUEgDH'
        access_token = '830480924479401984-wERHiXXjoDH0vDY2jvEfl31VC6wWR0s'
        access_token_secret = 'CrSChUizox55tDlZz5f6AOmYgRGxmljDAfLws5aWKPYMX'
 
       
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
 
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    
    def get_tweets_self(self, count = 10):
        tweets_self = []
        try:
            fetched_tweets = self.api.home_timeline(count = count)
            for tweet in fetched_tweets:
                tweets_self.append(self.clean_tweet(tweet.text))
            return tweets_self
        except tweepy.TweepError as e:
            print("Error : " + str(e))

    def get_tweets_other(self, name = '', count = 10):
        tweets_other = []
        try:
            fetched_tweets = self.api.user_timeline(screen_name = name, count = count)
            for tweet in fetched_tweets:
                tweets_other.append(self.clean_tweet(tweet.text))
            return tweets_other
        except tweepy.TweepError as e:
            print("Error : " + str(e))

    def get_trends(self):
        trendsName = []
        trends1 = self.api.trends_place(23424848)  # 23424848 is the WOEID for India
        data = trends1[0]
        trends = data['trends']
        for trend in trends:
            trendsName.append(trend['name'])
        return trendsName[:10]

@app.route("/" , methods=['POST'])
def handle_tweets():
    api = TwitterClient()
    req_data = request.get_json()
    choice = req_data['choice']
    user_param = req_data['user_param']
    if(choice == 1):    #self timeline
        tweets = api.get_tweets_self(count=10)
        Initialize.test_tweets_start.clear()
        Initialize.test_tweets_start.extend(tweets)
        # print(Initialize.test_tweets_start)
        analyzed1 = sentiment_mod.main()
        return jsonify({'self_analyzed' : analyzed1})
    elif(choice == 2):  #other timeline
        tweets = api.get_tweets_other(name=user_param, count=10)
        Initialize.test_tweets_start.clear()
        Initialize.test_tweets_start.extend(tweets)
        # print(Initialize.test_tweets_start)
        analyzed2 = sentiment_mod.main()
        return jsonify({'other_analyzed' : analyzed2})

    else:   #trends
        trends = api.get_trends()
        return jsonify({'trends' : trends})
    
if __name__ == "__main__":
    # calling main function
    # main()
    app.run(debug=True, port=5000)