#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 20:06:39 2018

@author: abha
"""


import pandas as pd



class Initialize:
    
    def init_train_tweets(tweets):
        train_tweets = []
        for (text, target) in tweets:
            words_filtered = [e.lower() for e in text.split() if len(e) >= 3]
            if(target == 0):
                target = 'negative'
            elif(target == 2):
                target = 'neutral'
            else:
                target = 'positive'
            train_tweets.append((words_filtered, target))
        #print(train_tweets[1:4])
    
    def init_test_tweets(tweets):
        test_tweets = []
        for(text) in tweets:
            words_filtered = [e.lower() for e in text.split() if len(e) >= 3]
            test_tweets.append((words_filtered))
        print(test_tweets[1:4])


def main():
    file = r'/home/abha/SE-Project-Twitzee-datasets/traintweets.csv'
    df = pd.read_csv(file, 
                     encoding='cp1252',  
                     names = ["target", "id", "date", "flag", "user", "text"])
    df1 = df[['text', 'target']]
    
    tweets = df1.values.tolist()
    Initialize.init_train_tweets(tweets)
    
    
if __name__ == "__main__": main()

    
    
    