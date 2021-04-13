#GETTING STARTED WITH TWEEPY
import tweepy 
import json
from Secret.tokens import APIKey, APISecretKey, AccessToken, AccessTokenSecret

#CREDENTIALS 
consumer_key = APIKey
consumer_secret = APISecretKey
access_token = AccessToken
access_token_secret = AccessTokenSecret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Getting information

# myData = api.me()

#Transforming data-> json
# data = json.dumps(myData._json, indent=2)
# print(data)
#Info de otro ususario
# userData = api.get_user(userAt)
# data = json.dumps(userData._json, indent=2)
# # print(data)

userAt = "EstefaniaLaver4"
limiteDeFollowers = 50
limiteDeAmigos = 50

def findFollowers(userAt, limite):
    userFollowers = [] #Seguidores del usuario
    userFollowersAt = [] #@ de los seguidores

    for user in tweepy.Cursor(api.followers, screen_name=userAt).items(limite):
        userFollowers.append(json.dumps(user._json, indent=2)) 
    
    for follower in userFollowers:
        follower = json.loads(follower)
        userFollowersAt.append(follower['screen_name'])
        # print('@', follower['screen_name'])

    return userFollowersAt

def findFriends(userAt,limite):
    friendsFollowing = [] #A quienes sigue el usuario
    friendsFollowingAt = [] #@ de amigos

    for user in tweepy.Cursor(api.friends, screen_name=userAt).items(limite):
        friendsFollowing.append(json.dumps(user._json, indent=2)) 

    for follower in friendsFollowing:
        follower = json.loads(follower)
        friendsFollowingAt.append(follower['screen_name'])
        # print('@', follower['screen_name'])

    return friendsFollowingAt

print(findFriends(userAt,limiteDeFollowers))
