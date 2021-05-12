#DEPENDENCIES
import json
import tweepy 
import time
from Secret.tokens import APIKey, APISecretKey, AccessToken, AccessTokenSecret

#CREDENTIALS AND AUTHENTICATION
consumer_key = APIKey
consumer_secret = APISecretKey
access_token = AccessToken
access_token_secret = AccessTokenSecret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#VARIABLES
userAt = "EstefaniaLaver4"
limiteDeFollowers = 30

#FUNCTIONS

def saveJson(data,fileName):
    #Data viene de la funcion direction
    file = open(fileName,"a+")
    file.write(data[0][0]+':\n')
    for element in data:
        file.write('    '+element[1]+'\n')

    file.close()

def direction(userAt, lista, t):
    friendToUser = []
    if t==1:
        for friend in lista:
            direction = (userAt, friend)
            friendToUser.append(direction)
    elif t==0:
        for friend in lista:
            direction = (friend,userAt)
            friendToUser.append(direction)
    return friendToUser

def findFollowers(userAt, limite):
    #Encuentra los seguidores del usuario y un limite de seguidores.
    userFollowersAt = [] #@ de los seguidores

    for user in tweepy.Cursor(api.followers, screen_name=userAt).items(limite):
        follower = json.loads(json.dumps(user._json, indent=2))
        userFollowersAt.append(follower['screen_name'])

    return userFollowersAt

def findAllFollowers(userAt, limiteFollowers, found, limite):
    followers = findFollowers(userAt,limiteFollowers)
    saveJson(direction(userAt,followers,1), "dataFollowers.txt")
    found.append(userAt)

    for i in range(0,limite):
        try:
            userAt = followers[i]
            if userAt not in found:
                followers += findFollowers(userAt,limiteFollowers)
                found.append(userAt)
                saveJson(direction(userAt,findFollowers(userAt,limiteFollowers),1), "dataFollowers.txt")
                followers.remove(userAt)
            else:
                continue
        except tweepy.RateLimitError:
            time.sleep(60 * 15)
            continue

# findAllFollowers(userAt,limiteDeFollowers,7)
# found=['marinapistacho','EstefaniaLaver4','auro_querol','BeaaM_','mnadalcalvo','CortizoKevin','PaNdA_Df','LaInvisible04','sebas7243','andreagomezjai1','Oscar_juli70','santiagozuiga7']
# found += ['RorroMC01','QuincyCoghill','Posue_Ronis','Gabriela_Musica','MeliValenez','jcastronauta','chuckygarcia','Toms90257478','SofaRubiano3','jaraalejo88','Juanpa15higuera','pau13_andrea','Saardiaz','Sofia_Lopez_07']
# findAllFollowers(userAt,limiteDeFollowers, found, 7)

def findFriends(userAt, limite):
    #Encuentra los seguidos por el usuario. En terminos de twitter los amigos.
    friendsFollowingAt = [] #@ de amigos

    for user in tweepy.Cursor(api.friends, screen_name=userAt).items(limite):
        friend = json.loads(json.dumps(user._json, indent=2))
        friendsFollowingAt.append(friend['screen_name'])

    return friendsFollowingAt
# findFriends(userAt,20)
def findAllFriends(userAt, limiteFriends, found, limite):
    friends = findFriends(userAt,limiteFriends)
    # saveJson(direction(userAt,friends,0), "dataFriends")
    # found.append(userAt)

    # for i in range(0,limite):
    #     try:
    #         userAt = friends[i]
    #         if userAt not in found:
    #             friends += findFriends(userAt,limiteFriends)
    #             found.append(userAt)
    #             saveJson(direction(userAt,findFollowers(userAt,limiteFriends),0), "dataFriends.txt")
    #             friends.remove(userAt)
    #         else:
    #             continue
    #     except tweepy.RateLimitError:
    #         time.sleep(60 * 15)
    #         continue
    # for user in found:
    #     try:
    #         userAt=user
    #         if userAt not in aux:
    #             friends += findFriends(userAt,limiteFriends)
    #             found.append(userAt)
    #             saveJson(direction(userAt,findFollowers(userAt,limiteFriends),0), "dataFriends.txt")
    #             friends.remove(userAt)
found = []
findAllFriends(userAt,limiteDeFollowers, found, 7)