#===DEPENDENCIES===
import json
import tweepy 
import time
from Secret.tokens import APIKey, APISecretKey, AccessToken, AccessTokenSecret

#===CREDENTIALS AND AUTHENTICATION===
consumer_key = APIKey
consumer_secret = APISecretKey
access_token = AccessToken
access_token_secret = AccessTokenSecret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#===VARIABLES===
userAt = "EstefaniaLaver4"
limiteDeFollowers = 30
limiteDeFriends = 30

#===FUNCTIONS===

def saveJson(data,fileName):
    #Data viene de la funcion direction
    file = open(fileName,"a+")
    file.write(data[0][0]+':\n')
    for element in data:
        file.write('    '+element[1]+'\n')

    file.close()

def saveJson2(data,fileName):
    #Data es una lista con direcciones de FRIENDS, p.ej [('marinapistacho', 'EstefaniaLaver4'), ('sebas7243', 'EstefaniaLaver4')]
    file = open(fileName,'a+')
    file.write(data[0][1]+':\n')
    for element in data:
        file.write('    '+element[0]+'\n')

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
                saveJson(direction(userAt,findFollowers(userAt,limiteFollowers),1), "APIinfo\dataFollowers.txt")
                followers.remove(userAt)
            else:
                continue
        except tweepy.RateLimitError:
            time.sleep(60 * 15)
            continue

def findFriends(userAt, limite):
    #Encuentra los seguidos por el usuario. En terminos de twitter los amigos.
    friendsFollowingAt = [] #@ de amigos

    for user in tweepy.Cursor(api.friends, screen_name=userAt).items(limite):
        friend = json.loads(json.dumps(user._json, indent=2))
        friendsFollowingAt.append(friend['screen_name'])

    return friendsFollowingAt

def findAllFriends(listaFollowers, limiteDeFriends):
    #Lista followers es la lista de usuarios a los que se les buscaron los followers

    for userAt in listaFollowers:
        try:
            friends = findFriends(userAt,limiteDeFriends)
            saveJson2(direction(userAt,friends,0), "APIinfo\dataFriends.txt")
        except tweepy.RateLimitError:
            time.sleep(60*15)
            continue

#===TESTS===
# findAllFollowers(userAt,limiteDeFollowers,7)
found = ['marinapistacho','EstefaniaLaver4','auro_querol','BeaaM_','mnadalcalvo','CortizoKevin','PaNdA_Df','LaInvisible04','sebas7243','andreagomezjai1','Oscar_juli70','santiagozuiga7','RorroMC01','QuincyCoghill','Posue_Ronis','Gabriela_Musica','MeliValenez','jcastronauta','chuckygarcia','Toms90257478','SofaRubiano3','jaraalejo88','Juanpa15higuera','pau13_andrea','Saardiaz','Sofia_Lopez_07']
#findAllFollowers(userAt,limiteDeFollowers, found, 7)
# print(findFriends(userAt,limiteDeFollowers))

test = [('marinapistacho', 'EstefaniaLaver4'), ('sebas7243', 'EstefaniaLaver4'), ('Gabriela_Musica', 'EstefaniaLaver4'), ('andreagomezjai1', 'EstefaniaLaver4'), ('VarunSaranga', 'EstefaniaLaver4'), ('baumanelise', 'EstefaniaLaver4'), ('realtimrozon', 'EstefaniaLaver4'), ('darmenteras', 'EstefaniaLaver4'), ('WynonnaEarp', 'EstefaniaLaver4'), ('MelanieScrofano', 'EstefaniaLaver4'), ('KatBarrell', 'EstefaniaLaver4'), ('emtothea', 'EstefaniaLaver4'), 
('DominiqueP_C', 'EstefaniaLaver4'), ('elijahdaniel', 'EstefaniaLaver4'), ('doddleoddle', 'EstefaniaLaver4'), ('natvanlis', 'EstefaniaLaver4'), ('alexpapiccio', 'EstefaniaLaver4'), ('ArianaGrande', 'EstefaniaLaver4'), ('Camila_Cabello', 'EstefaniaLaver4'), ('Normani', 'EstefaniaLaver4'), ('dinahjane97', 'EstefaniaLaver4'), ('HayleyKiyoko', 'EstefaniaLaver4'), ('AllyBrooke', 'EstefaniaLaver4'), ('RoseEllenDix', 'EstefaniaLaver4'), ('stevieboebi', 'EstefaniaLaver4'), ('cammiescott', 'EstefaniaLaver4'), ('LaurenJauregui', 'EstefaniaLaver4'), ('allyhills', 'EstefaniaLaver4'), ('nowthisisliving', 'EstefaniaLaver4'), ('findingfletcher', 'EstefaniaLaver4')] 
# saveJson2(test,"dataFriends.txt")
findAllFriends(found,limiteDeFriends)