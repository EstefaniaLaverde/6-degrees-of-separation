import networkx as nx
import matplotlib.pyplot as plt

N1 = ['A','B','C','D','E']
N2 = ['F','G','H','I','J']
N5 = ['K','L','M','N','O']

N3=["1"]

N4=["2"]

N6=["3"]


L1=[(N1[i],N3[0]) for i in range(0,len(N1))]

L2=[(N2[j],N4[0]) for j in range(0,len(N2))]

L3=[(N5[k],N6[0]) for k in range(0,len(N5))]


L4=list(zip(N3,N4))
L5=list(zip(N3,N6))

G1 = nx.DiGraph()
G1.add_edges_from(L1)
pos = nx.spring_layout(G1)
nx.draw_networkx_nodes(G1, pos, node_size=400, node_color="green",edgecolors=("green"))
nx.draw_networkx_edges(G1, pos, edgelist=G1.edges(),edge_color='green')
nx.draw_networkx_labels(G1, pos, font_size=10,font_color="white")
plt.show()



G2 = nx.DiGraph()
G2.add_edges_from(L2)
pos = nx.spring_layout(G2)
nx.draw_networkx_nodes(G2, pos, node_size=400, node_color="blue",edgecolors=("blue"))
nx.draw_networkx_edges(G2, pos, edgelist=G2.edges(),edge_color='black')
nx.draw_networkx_labels(G2, pos, font_size=10,font_color="white")
plt.show()



G3 = nx.DiGraph()
G3.add_edges_from(L4)


G4 = nx.DiGraph()
G4.add_edges_from(L3)
pos = nx.spring_layout(G4)
nx.draw_networkx_nodes(G4, pos, node_size=800, node_color="red",edgecolors=("red"))
nx.draw_networkx_edges(G4, pos, edgelist=G4.edges(),edge_color='red')
nx.draw_networkx_labels(G4, pos, font_size=10,font_color="white")
plt.show()

G5 = nx.DiGraph()
G5.add_edges_from(L5)

G = nx.DiGraph()
G=nx.compose_all([G1,G2,G3,G4,G5])
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=400, node_color="black",edgecolors=("black"))
nx.draw_networkx_edges(G, pos, edgelist=G.edges(),edge_color='black')
nx.draw_networkx_labels(G, pos, font_size=10,font_color="white")
plt.show()


print(nx.info(G))
nx.draw_circular(G,with_labels=True)
#print("Grados de cada vertice:",nx.degree(G))
