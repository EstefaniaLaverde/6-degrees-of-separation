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
userAt = "jaraalejo88"
limiteDeFollowers = 30

#FUNCTIONS

def saveJson(data,fileName):
    #Data viene de la funcion direction
    file = open(fileName,"a+")
    file.write(data[0][0]+':\n')
    for element in data:
        file.write('    '+element[1]+'\n')

    file.close()

def direction(userAt, lista):
    friendToUser = []

    for friend in lista:
        direction = (userAt, friend)
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
    saveJson(direction(userAt,followers), "dataFollowers")
    found.append(userAt)

    for i in range(0,limite):
        try:
            userAt = followers[i]
            if userAt not in found:
                followers += findFollowers(userAt,limiteFollowers)
                found.append(userAt)
                saveJson(direction(userAt,findFollowers(userAt,limiteFollowers)), "dataFollowers")
                followers.remove(userAt)
            else:
                continue
        except tweepy.RateLimitError:
            time.sleep(60 * 15)
            continue

# findAllFollowers(userAt,limiteDeFollowers,7)
found=['marinapistacho','EstefaniaLaver4','auro_querol','BeaaM_','mnadalcalvo','CortizoKevin','PaNdA_Df','LaInvisible04','sebas7243','andreagomezjai1','Oscar_juli70','santiagozuiga7']
found += ['RorroMC01','QuincyCoghill','Posue_Ronis','Gabriela_Musica','MeliValenez','jcastronauta','chuckygarcia','Toms90257478','SofaRubiano3','jaraalejo88','Juanpa15higuera','pau13_andrea','Saardiaz','Sofia_Lopez_07']
findAllFollowers(userAt,limiteDeFollowers, found, 7)

