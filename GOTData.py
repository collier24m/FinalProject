#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:48:32 2019

@author: matthewcollier
"""

import tweepy
from textblob import TextBlob
import unicodedata

####input your credentials here
consumer_key = 'TCYJzim4QjEF4FCpdAmbNOL8E'
consumer_secret = '07Pccyv2CQclUGjnqQq6uMwAtbkDA7tppLBWIdZLFtkCr9nDTi'
access_token = '305369952-cLUBcuQ2MeHpnNAptNs8nG3C0fskXTsdzVajzeo0'
access_token_secret = 'jDiEszg3o91yKIh1rVW5Xhwbkfn3I9bBBmqjJ6Ik0uqQ2'




####Authentication for access of API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

###Episode Variables for Cursor.since attribute
Episode1 = "2019-04-14"
Episode2 = "2019-04-21"
Episode3 = "2019-04-28"
Episode4 = "2019-05-05"
Episode5 = "2019-05-12"
Episode6 = "2019-05-19" 


### Function for getting Cersei's Tweets      
def CerseiTweets():
    with open("CerseiTweets.txt", "w") as txtfile:
        print("Grabbing Twitter Data \n")
        for tweet in tweepy.Cursor(api.search,q='cersei lannister',
                               lang="en",
                               since=Episode1).items(100):
            txtfile.write(str(unicodedata.normalize('NFKD', tweet.text).encode('ascii','ignore')) + "\n")
                
    print("Finished \n")


### Sentiment/Polarity Analysis of Cersei    
def SentimentCersei():    
    CersiSentiment = 0.0
    with open("JonTweets.txt", "r") as txtfile:    
        for line in txtfile:
            line = str(line)
            analysis = TextBlob(line)
            CersiSentiment += analysis.sentiment.polarity
            totalSentiment = CersiSentiment
    print("Cersi's Polarity:" + str(totalSentiment))        
    if totalSentiment > 1:
        print("People have a POSITIVE opinion of Cersei Lannaster \n")
    elif totalSentiment < 1 and totalSentiment > -1 :
        print("People have a Netural View of Cersei Lannaster \n")
    else:
        print("People have a NEGATIVE view of Cersei Lannaster \n")


#############################################################################
        
        
### Function for getting Sansa's Tweets    
def SansaTweets(): 
    with open("SansaTweets.txt", "w") as txtfile:
        print("Grabbing Twitter Data \n")
        for tweet in tweepy.Cursor(api.search,q='sansa stark',
                               lang="en",
                               since=Episode1).items(100):
            txtfile.write(str(unicodedata.normalize('NFKD', tweet.text).encode('ascii','ignore')) + "\n")
    print("Finished \n")
   
    
### Sentiment/Polarity Analysis of Sansa        
def SentimentSansa():    
    SansaSentiment = 0.0
    with open("SansaTweets.txt", "r") as txtfile:    
        for line in txtfile:
            line = str(line)
            analysis = TextBlob(line)
            SansaSentiment += analysis.sentiment.polarity
            totalSentiment = SansaSentiment
    print("Sansa's Polarity: " + str(totalSentiment)) 
    if totalSentiment > 1:
        print("People have a POSITIVE opinion of Sansa Stark \n")
    elif totalSentiment < 1 and totalSentiment > -1 :
        print("People have a Netural View of Sansa Stark \n")
    else:
        print("People have a NEGATIVE view of Sansa Stark \n")
############################################################################
        
        
### Function for getting Jons's Tweets    
def JonTweets(): 
    with open("JonTweets.txt", "w") as txtfile:
        print("Grabbing Twitter Data \n")
        for tweet in tweepy.Cursor(api.search,q='jon snow',
                               lang="en",
                               since=Episode1).items(100):
            txtfile.write(str(unicodedata.normalize('NFKD', tweet.text).encode('ascii','ignore')) + "\n")
    print("Finished \n")  
    
    
### Sentiment/Polarity Analysis of Jon    
def SentimentJon():    
    JonSentiment = 0.0
    with open("CerseiTweets.txt", "r") as txtfile:    
        for line in txtfile:
            line = str(line)
            analysis = TextBlob(line)
            JonSentiment += analysis.sentiment.polarity
            totalSentiment = JonSentiment
    print("Jon's Polarity: " + str(totalSentiment))
    if totalSentiment > 1:
        print("People have a POSITIVE opinion of Jon Snow \n")
    elif totalSentiment < 1 and totalSentiment > -1 :
        print("People have a Netural View of Jon Snow \n")
    else:
        print("People have a NEGATIVE view of Jon Snow \n")
########################################################################

### Main Funciton
def main():
    CerseiTweets()
    JonTweets()
    SansaTweets()
    SentimentCersei()
    SentimentJon()
    SentimentSansa()
    

if __name__ == '__main__':
    main()


       
