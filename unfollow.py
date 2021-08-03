import requests,json,sys
import time
import tweepy


if __name__ == '__main__':
    CONSUMER_KEY = 'CONSUMER_KEY'
    CONSUMER_SECRET = 'CONSUMER_SECRET'
    ACCESS_TOKEN = 'ACCESS_TOKEN'
    ACCESS_TOKEN_SECRET = 'ACCESS_TOKEN_SECRET'

    TwitterAuth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    TwitterAuth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    try:
        api = tweepy.API(TwitterAuth)
        followers = api.followers_ids()
        following = api.friends_ids()
  
        for following in following:
            if following not in followers:
                api.destroy_friendship(following)
    
    except Exception as e:
        print(e)