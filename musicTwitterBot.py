import tweepy, time, sys
import json
import urllib2
import unicodedata
import math


#Authorization
APP_KEY = 'app_key'
APP_SECRET = 'app_secret'
OAUTH_TOKEN = 'oauth_token'
OAUTH_TOKEN_SECRET = 'oauth_token_secret'
auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)


#Establish Followers
followers = api.followers_ids('your_twitter_account')
friends = api.friends_ids('yout_twitter_account')




def tweetToFollowers():
    for f in friends:
        myFollowers = format(api.get_user(f).screen_name)
        

#pull song from last.fm and tweet the song artitist and link.        
def nowPlaying():
    url = 'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=leavenstee&limit=1&api_key=API_KEYa&format=json'
    data = json.loads(urllib2.urlopen(url).read())
    try:
        artist =  data['recenttracks']['track']['artist']['#text']
        song = data['recenttracks']['track']['name']
        api.update_status("#np " + song + " by " + artist)
        print song
    except (ValueError, TypeError, KeyError):
        nowPlaying()
        
        
def printFollowers():
    follow2 = api.followers_ids() # gives a list of followers ids
    print "you have %d followers" % len(follow2)
    

def followFollowers():
    nowPlaying()
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        newFollower = follower.screen_name
    time.sleep(300)
    followFollowers()

def location():
    hey = raw_input("Where are you listening to music: ")
    if hey == "0":
        print "RESTARTED"
    else:
        api.update_status("Now live at " + hey)


location()
printFollowers()
followFollowers()
