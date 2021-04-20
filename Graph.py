#GETTING STARTED WITH TWEEPY
import tweepy 
import json
""" Si eres Estefania no olvides agregar el "Secrets." en la siguiente linea """
from tokens import APIKey, APISecretKey, AccessToken, AccessTokenSecret
import networkx as nx
import matplotlib.pyplot as plt

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

#L2=[userAt]

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

def recursiveFindFollowers(userAt,limiteDeFollowers, limiteIt):
    it = 0
    userFollowersAt = findFollowers(userAt,limiteDeFollowers)

    for follower in userFollowersAt: #seguidores del usuario inicial
        it+=1
        fFollowers = findFollowers(follower, limiteDeFollowers)

        for i in range(limiteIt-1):
            userToFollower()
        # print(findFollowers(follower, limiteDeFollowers))
    return fFollowers

    

#TESTS
print("_______________________________________________________________________")
print(findFriends(userAt,limiteDeFollowers))
print("_______________________________________________________________________")
print(friendToUser(userAt,limiteDeFollowers))

print("_______________________________________________________________________")
print("___________________________RECURSUVA_____________________________")
print("_______________________________________________________________________")

print (recursiveFindFollowers(userAt,limiteDeFollowers, 1))

###############################################################################
###############################################################################

L1=findFriends(userAt,limiteDeFollowers)

#Lista para realizar el grafo
#L=[(L2[0],L1[i]) for i in range(0,len(L1))]
# print("________________________LLLLLLLLLLLLLLLLLLLL____________________________")
# print(L)

print("_______________________________________________________________________")
print("___________________________graficando ando_____________________________")
print("_______________________________________________________________________")

#L=list(zip(findFriends(userAt,limiteDeFollowers),userAt))

""" Se grafica """

G = nx.DiGraph()
G.add_edges_from(friendToUser(userAt,limiteDeFollowers))
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=400, node_color="blue",edgecolors=("blue"))
nx.draw_networkx_edges(G, pos, edgelist=G.edges(),edge_color='green')
nx.draw_networkx_labels(G, pos, font_size=10,font_color="black")
plt.show()
print(nx.info(G))
print("Grados de cada vertice:",nx.degree(G))
#nx.draw_circular(G,with_labels=True)
