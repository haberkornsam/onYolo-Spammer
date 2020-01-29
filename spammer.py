import os
import tweepy
import random


yoloURL = '' #the url used to attach the yolo dialog to snapchat
yoloUserCode = '' #the code in the url following /m/ and before ?w
initialMsg = 'This is a friendly reminder that this is really annoying on your story. Prepare to be spammed with tweets from president Donald J Trump!'
twitterUser = 'realdonaldtrump'
tweetQuantity = 200



consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api=tweepy.API(auth)

# initialize a list to hold all the tweepy Tweets
alltweets=[]

new_tweets=api.user_timeline(screen_name=twitterUser, count=tweetQuantity, include_rts = True)

# save most recent tweets
alltweets.extend(new_tweets)

outtweets = [tweet.text.encode("utf-8") for tweet in alltweets]

print(outtweets)

import requests



cookies = {
    'popshow-temp-id': 'ss3iz6y2hwgs1g3mwkgp9q',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/json;charset=utf-8',
    'Origin': 'https://onyolo.com',
    'Connection': 'keep-alive',
    'Referer': yoloURL,
}

data = '{"text":"'+initialMsg+'","cookie":"ss3iz6y2hwgs1g3mwkgp9q","wording":"Send me honest messages"}'

response = requests.post('https://onyolo.com/'+yoloUserCode+'/message', headers=headers, cookies=cookies, data=data)


print(len(outtweets))

for t in outtweets:

    tweett=t.decode('utf-8')

    data = '{"text":"'+tweett+'","cookie":"ss'
    data += str(random.randrange(1,9))
    data += 'in'
    data += str(random.randrange(1,9))
    data += 'y2hwgs1g3mwkgp9q","wording":"Send me honest messages"}'
    try:
        pass
        #response = requests.post('https://onyolo.com/'+yoloUserCode+'/message', headers=headers, cookies=cookies, data=data)
    except:
        pass
