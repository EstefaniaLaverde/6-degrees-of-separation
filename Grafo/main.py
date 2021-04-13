#GETTING STARTED WITH TWEEPY

import tweepy 
import json
from tokens import APIKey, APISecretKey, AccessToken, AccessTokenSecret

#CREDENTIALS 
consumer_key = APIKey
consumer_secret = APISecretKey
access_token = AccessToken
access_token_secret = AccessTokenSecret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Getting information

myData = api.me()

#Transforming data-> json
# data = json.dumps(myData._json, indent=2)
# print(data)

#Info de otro ususario
nikeData = api.get_user('nike')
data = json.dumps(nikeData._json, indent=2)
print(data)

#Followers de un usuario
# data = api.followers(screen_name="nike") #Solo trae de a 20 usuarios

limiteDeFollowers = 25
# for user in tweepy.Cursor(api.followers, screen_name="nike").items(limiteDeFollowers):
#     print(json.dumps(user._json, indent=2))

#Followees del usuarios
# misSeguidores = tweepy.Cursor(api.followers, screen_name="EstefaniaLaver4").items(limiteDeFollowers)
# seguidor1 = json.dumps(misSeguidores[0]._json, indent=2)
# for user in misSeguidores:
#     print(json.dumps(user._json, indent=2))
# print(seguidor1) 