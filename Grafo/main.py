#DEPENDENCIES
import json
import tweepy 
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
limiteDeFollowers = 30
limiteDeAmigos = 30
limiteIt = 50

listaUsersFollowers = [userAt]
listaUsersFriends = [userAt]

#FUNCTIONS
def saveJson(data):
    #Data viene de la funcion direction
    file = open("jsonData.txt","a+")
    file.write(data[0][0]+':\n')
    for element in data:
        file.write('    '+element[1]+'\n')

    file.close()

def saveJson2(data):
    #Data viene de la funcion direction
    file = open("jsonData2.txt","a+")
    file.write(data[0][0]+':\n')
    for element in data:
        file.write('    '+element[1]+'\n')

    file.close()

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

def direction(userAt, lista):
    friendToUser = []

    for friend in lista:
        direction = (userAt, friend)
        friendToUser.append(direction)
    return friendToUser


def findAllFollowerConnection(linea):
    file = open("jsonData.txt","r")
    lines = file.readlines()

    for i in range(linea+1,len(lines)):
        # linea +=len(lines)-linea
        linea +=1
        if lines[i].strip('    ').strip('\n').strip(':') not in listaUsersFollowers:
            listaUsersFollowers.append(lines[i].strip('    ').strip('\n').strip(':'))
            userAt = listaUsersFollowers[-1]

            #Buscando los followers
            listaUsersFollowers.append(userAt)
            userFollowersAt = findFollowers(userAt, limiteDeFollowers)
            data = direction(userAt,userFollowersAt)
            saveJson(data)

            print(userAt)
        else:
            linea+=1

def findAllFriendsConnection(linea):
    file = open("jsonData2.txt","r")
    lines = file.readlines()

    for i in range(linea+1,len(lines)):
        # linea +=len(lines)-linea
        linea +=1
        if lines[i].strip('    ').strip('\n').strip(':') not in listaUsersFriends:
            listaUsersFriends.append(lines[i].strip('    ').strip('\n').strip(':'))
            userAt = listaUsersFriends[-1]

            #Buscando los followers
            listaUsersFriends.append(userAt)
            userFriendsAt = findFriends(userAt, limiteDeFollowers)
            data = direction(userAt,userFriendsAt)
            saveJson(data)

        else:
            linea+=1

def main():
    it1=0
    linea1 = 0
    # listaUsersFollowers.append(userAt)
    userFollowersAt = findFollowers(userAt, limiteDeFollowers)
    data = direction(userAt,userFollowersAt)
    saveJson(data)

    while it1<limiteIt:
        it1+=1
        findAllFollowerConnection(linea1)

    it2=0
    linea2 = 0
    # listaUsersFriends.append(userAt)
    userFriendsAt = findFriends(userAt, limiteDeAmigos)
    data = direction(userAt,userFriendsAt)
    saveJson(data)

    while it2<limiteIt:
        it+=1
        findAllFriendsConnection(linea2)





#TESTS
# print(findFriends(userAt,limiteDeFollowers))

# print(friendToUser(userAt,findFriends(userAt, limiteDeAmigos)))
# saveJson(direction(userAt,findFriends(userAt, limiteDeAmigos)))

# recursiveFindFollowers(userAt,limiteDeFollowers, 1)

# findAllFollowerConnection(userAt, limiteDeFollowers, 3)

# print(direction(userAt,findFriends(userAt, limiteDeAmigos)))

main()