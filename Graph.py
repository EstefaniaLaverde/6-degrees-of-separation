import networkx as nx
import matplotlib.pyplot as plt

N1 = ['A','B','C','D','E']
N2 = ['G','G','G','G','G']

L=list(zip(N2,N1))


# list_a = [1, 2, 3, 4]
# list_b = [5, 6, 7, 8]
# list_c=[(list_a[i],list_b[i]) for i in range(0,len(list_a))]


G = nx.DiGraph()
G.add_edges_from(L)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=400, node_color="green",edgecolors=("blue"))
nx.draw_networkx_edges(G, pos, edgelist=G.edges(),edge_color='red')
nx.draw_networkx_labels(G, pos, font_size=10,font_color="white")
plt.show()
print(nx.info(G))
