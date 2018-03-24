#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 20:06:39 2018

@author: abha
"""
import nltk
import pandas as pd
import re



init_train =[]
word_features = []
class Initialize:

    test_tweets_start = []


    def init_test_tweets(self, tweets):
        test_tweets = []
        for(text) in tweets:
            words_filtered = [e.lower() for e in text.split() if len(e) >= 3]
            test_tweets.append((words_filtered))
        # print(test_tweets[1:4])
        return test_tweets

    def init_train_tweets(self, tweets):
        train_tweets = []
        for (text, target) in tweets:
            words_filtered = [e.lower() for e in text.split() if len(e) >= 3]
            if (target == 0):
                target = 'negative'
            elif (target == 2):
                target = 'neutral'
            else:
                target = 'positive'
            train_tweets.append((words_filtered, target))
        return train_tweets
        # print(train_tweets[1:4])

    def get_words(self, tweets):
        all_words = []
        for (words, sentiment) in tweets:
            all_words.extend(words)
        return all_words

    def get_words_features(self, tweets):
        words_list = nltk.FreqDist(self.get_words(tweets))
        words_features = words_list.keys()
        return words_features

    def extract_features(document):
        document_words = set(document)
        features = {}
        for word in word_features:
            features['contains(%s)' % word] = (word in document_words)
        return features

    def __init__(self, tweets):     #training
        inittrain = self.init_train_tweets(tweets)
        init_train.extend(inittrain)
        #inittest = self.init_test_tweets(self.test_tweets_start)    #UNCOMMENT THIS

        inittest = [
            ['the', 'would', 'safer', 'place', 'thousands', 'guns', 'weren', 'sold', 'every', 'day', 'without',
             'background', 'checks'],
            ['donald', 'trump', 'takes', 'hard', 'look', 'himself', 'new', 'simpsons', 'sketch'],
            ['desperate', 'for', 'victory', 'aussies', 'back', 'cheating', 'suspected', 'ball', 'tampering', 'bancroft',
             'caught', 'tape', 'cau']]    #COMMENT THIS


        #features_train = self.get_words_features(inittrain)
        word_features.extend(self.get_words_features(inittrain))
        #training_set = nltk.classify.apply_features(extract_features(), inittrain)
        #print(training_set[1:4])

        #print(self.extract_features(inittrain))








def main():

    file = r'/home/abha/SE-Project-Twitzee-datasets/traintweets.csv'
    df = pd.read_csv(file,
                    encoding='cp1252',
                    names = ["target", "id", "date", "flag", "user", "text"])
    df1 = df[['text', 'target']]

    tweets = df1.values.tolist()

    Initialize(tweets)
    training_set = nltk.classify.apply_features(Initialize.extract_features, init_train)
    print(training_set[1:4])





    
    
if __name__ == "__main__": main()

    
    
    