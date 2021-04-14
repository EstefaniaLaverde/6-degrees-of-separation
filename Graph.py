#GETTING STARTED WITH TWEEPY
import tweepy 
import json
import networkx as nx
import matplotlib.pyplot as plt

""" Si eres Estefania no olvides agregar el "Secrets." en la siguiente linea """

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

# myData = api.me()

#Transforming data-> json
# data = json.dumps(myData._json, indent=2)
# print(data)
#Info de otro ususario
# userData = api.get_user(userAt)
# data = json.dumps(userData._json, indent=2)
# # print(data)

userAt = "EstefaniaLaver4"

L2=[userAt]

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

L1=findFriends(userAt,limiteDeFollowers)

#Lista para realizar el grafo
L=[(L2[0],L1[i]) for i in range(0,len(L1))]

print(L)

print("_______________________________________________________________________")
print("graficando ando")
print("_______________________________________________________________________")

#L=list(zip(findFriends(userAt,limiteDeFollowers),userAt))



G = nx.DiGraph()
G.add_edges_from(L)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=400, node_color="blue",edgecolors=("blue"))
nx.draw_networkx_edges(G, pos, edgelist=G.edges(),edge_color='red')
nx.draw_networkx_labels(G, pos, font_size=10,font_color="black")
plt.show()
print(nx.info(G))
print("Grados de cada vertice:",nx.degree(G))
#nx.draw_circular(G)
