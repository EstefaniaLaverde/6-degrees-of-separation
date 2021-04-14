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

#VARIABLES
userAt = "EstefaniaLaver4"
limiteDeFollowers = 50
limiteDeAmigos = 50

#FUNCTIONS
def findFollowers(userAt, limite):
    #Encuentra los seguidores del usuario y un limite de seguidores.
    userFollowersAt = [] #@ de los seguidores

    for user in tweepy.Cursor(api.followers, screen_name=userAt).items(limite):
        follower = json.loads(json.dumps(user._json, indent=2))
        userFollowersAt.append(follower['screen_name'])

    return userFollowersAt

def findFriends(userAt, limite):
    #Encuentra los seguidos por el usuario. En terminos de twitter los amigos.
    friendsFollowingAt = [] #@ de amigos

    for user in tweepy.Cursor(api.friends, screen_name=userAt).items(limite):
        friend = json.loads(json.dumps(user._json, indent=2))
        friendsFollowingAt.append(friend['screen_name'])

    return friendsFollowingAt

def userToFollower(userAt, limiteFollowers):
    userToFollower = []
    userFollowersAt = findFollowers(userAt,limiteDeFollowers)

    for follower in userFollowersAt:
        direction = (follower, userAt)
        userToFollower.append(direction)
    return userToFollower

def friendToUser(userAt, limiteFollowing):
    friendToUser = []
    friendsFollowingAt = findFriends(userAt,limiteDeAmigos)

    for friend in friendsFollowingAt:
        direction = (userAt, friend)
        friendToUser.append(direction)
    return friendToUser

# def recursiveFindFollowers(userAt,limiteDeFollowers, limiteIt):
#     it = 0
#     userFollowersAt = findFollowers(userAt,limiteDeFollowers)

#     for follower in userFollowersAt: #seguidores del usuario inicial
#         it+=1
#         fFollowers = findFollowers(follower, limiteDeFollowers)

#         for i in range(limiteIt-1):
#             userToFollower()
#         # print(findFollowers(follower, limiteDeFollowers))



#TESTS
# print(findFriends(userAt,limiteDeFollowers))

# print(friendToUser(userAt,limiteDeFollowers))

# recursiveFindFollowers(userAt,limiteDeFollowers, 1)

