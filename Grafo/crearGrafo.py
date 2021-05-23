from os import linesep, name
import igraph as ig
import cairo as cr
from math import comb

"""=== MANEJO DE LA INFORMACION OBTENIDA DE LA API ==="""

file = open("APIinfo\dataFollowers.txt",'r')
fLines = file.readlines()

listUsers = []
for line in fLines:
    if line[0] != " ":
        listaAux = []
        listUsers.append(listaAux)
        listaAux.clear()
        listaAux.append(line.strip('\n').strip(':'))
    elif line[0] == " ":
        listaAux.append(line.strip('    ').strip('\n'))

#print(listUsers)

direcciones1 = [] #LISTA CON LAS DIRECCIONES DE LOS FOLLOWERS
for lista in listUsers:
    centralNode = lista[0]
    lista.remove(centralNode)
    for user in lista:
        direcciones1.append((centralNode,user))

file.close()

file = open("APIinfo\dataFriends.txt",'r')
ffLines = file.readlines()


listFriends = []

for line in ffLines:
    if line[0] != " ":
        listaAux = []
        listFriends.append(listaAux)
        listaAux.clear()
        listaAux.append(line.strip('\n').strip(':'))
    elif line[0] == " ":
        listaAux.append(line.strip('    ').strip('\n'))

direcciones2 = [] #LISTA CON LAS DIRECCIONES DE LOS FOLLOWERS
for lista in listFriends:
    centralNode = lista[0]
    lista.remove(centralNode)
    for user in lista:
        direcciones2.append((user,centralNode))

file.close()


direcciones = direcciones1 + direcciones2 #Lista con toda la información recolectada

"""=== FUNCION PARA CREAR EL GRAFO ==="""
def createGraph(listaDirecciones):

    #INPUT:
    #   listaDirecciones: lista con los nodos y la direccion, p.ej [(pepe,pepa),(juan,jose)]
    #OUTPUT:
    #   grafo formado a partir de la lista

    nodes = []
    edges = []
    for direction in listaDirecciones:
        nodo1 = direction[0]
        nodo2 = direction[1]

        #Lista de los nodos
        if nodo1 not in nodes:
            nodes.append(nodo1)
        if nodo2 not in nodes:
            nodes.append(nodo2)

        #Añadir aristas
        indexNodo1 = nodes.index(nodo1)
        indexNodo2 = nodes.index(nodo2)

        edges.append((indexNodo2,indexNodo1))


    graph = ig.Graph(n=len(nodes), vertex_attrs = {'name':nodes}, directed = True, edges = edges)
    graph.es["weight"] = 1.0

    return graph, nodes

"""=== CREACION DEL GRAFO ==="""

gr , visited = createGraph(direcciones) #No dirigido
g_dir , visited = createGraph(direcciones) #Dirigido

gr.to_undirected(mode='collapse', combine_edges=None)


"""=== FUNCION PARA OBTENER LAS DISTANCIAS ==="""
def SeisGrados(graficar):
    
        #INPUT:
    #   graficar: T -> Grafica en el archivo 'Camino.png' el camino mas corto entre los vertices
    #              F -> Imprime la longitud del camino mas corto


    origen=input("Origen: ")
    destino=input("Destino: ")
    camino = gr.shortest_paths(source=origen, target=destino, mode='out')

    if graficar == True:
        caminoVertices = gr.get_shortest_paths(v=origen, to=destino,mode='out',output='vpath')[0]

        names = []
        dirAux = []
        for i in range(0,len(caminoVertices)):
            gr.vs[caminoVertices[i]]["color"] = "blue"
            if i != len(caminoVertices)-1:
                nombre1 = gr.vs[caminoVertices[i]].attributes()['name']
                nombre2 = gr.vs[caminoVertices[i+1]].attributes()['name']
                if nombre1 not in names:
                    names.append(nombre1)
                if nombre2 not in names:
                    names.append(nombre2)
                
                id_arista = gr.get_eid(caminoVertices[i], caminoVertices[i+1])
                gr.es[id_arista]["color"] = "blue"
                dirAux.append((names.index(nombre1),names.index(nombre2)))
        #Cambiar color de el grafo principal
        ig.plot(gr, layout = gr.layout_davidson_harel(),target='Graficas\grafoCamino.png',bbox = (4000, 4000), margin = 20,vertex_label=visited)
        #Crear el grafo
        grafoAux = ig.Graph(n=len(names), vertex_attrs = {'name':names},edges = dirAux)
        ig.plot(grafoAux,layout=gr.layout_reingold_tilford_circular(),target='Graficas\Camino.png',bbox = (1000, 1000), margin = 10 ,vertex_label=names)
    print("La longitud del camino es de:", camino[0][0])

SeisGrados(True)

"""------------------------ layouts ---------------------------"""
#layout = gr.layout('grid_fr')
##layout= gr.layout_davidson_harel()
#layout= gr.layout_graphopt()
#layout= gr.layout_lgl()
#layout= gr.layout_reingold_tilford_circular()
#layout= gr.layout_sugiyama()

"""------------------------- Graficas --------------------------"""
# ig.plot(gr, layout = layout,target='Graficas\grafo.png',bbox = (4000, 4000), margin = 20,vertex_label=visited)
# ig.plot(g_dir, layout = layout,target='Graficas\digrafo.png',bbox = (4000, 4000), margin = 20,vertex_label=visited)
"""------------------------- Numeros --------------------------"""
N_V = gr.vcount()
#N_E = gr.ecount()

#print("Numero de vertices = ", N_V)
#print("Numero de aristas = ", N_E)


"""=== INFORMACION DEL GRAFO ==="""
# Corto1=gr.shortest_paths(source=None, target=None, mode='out')
# #print("shortest_paths: ",Corto1)
# index = 0
# for path in Corto1:
#     print(visited[index],":",max(path))
#     index +=1

# a=0
# for path in Corto1:
#     a+=sum(path)


# suma1=0
# suma2=0
# for path in Corto1:
#     suma1 += sum(path)
#     suma2 += len(path)
#     prom = suma1/suma2

# print("Indice de Wiener",a)
# #print(Corto1)
# print("Promedio shortest_paths: ", prom )
# eccen = gr.eccentricity(vertices=None, mode='all')
# # print("Eccentricity: ", eccen)

# vertMini = []
# mini = min(eccen)
# i=0
# for eccvert in eccen:
#     if eccvert == mini:
#         vertMini.append(i)
#     i+=1

# # print("Min EEE: ", mini)
# print("Vertices de minima excentricidad: ",vertMini)
# centro = gr.induced_subgraph(vertMini, implementation='auto')
# print("Centro", centro)
# print("Max EEE: ", max(gr.eccentricity(vertices=None, mode='all')))
# print("Radio: ", gr.radius(mode='all'))
# print("Diametro: ", gr.diameter(directed=False, unconn=True, weights=None))
# print("Get_Diametro: ", gr.get_diameter(directed=False, unconn=True, weights=None))
# print("Cintura_F: ", gr.girth(return_shortest_circle=False))
# print("Cintura_T: ", gr.girth(return_shortest_circle=True))
# print("Distancia Promedio: ", a/(comb(N_V,2)))


"""--------------------------------------------------------"""
"""-------------------------TESTS--------------------------"""
"""--------------------------------------------------------"""
#print(len(Corto1[0]))

#Corto2 = gr.get_shortest_paths(v='sebas7243', to=None,mode='out',output='vpath')
#print("get_shortest_paths: ", Corto2)

#print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
#print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
#Corto3 = gr.get_all_shortest_paths(v='sebas7243', to=None,mode='all')
#print("get_all_shortest_paths: ", Corto3)

#print(visited)
#print(gr.vs[31])



#ig.plot(gr, layout = layout,target='myfile.png',bbox = (2000, 2000),
#        margin = 20, vertex_color = "green",edge_width=2,
#        edge_arrow_width = 100,vertex_label=visited) #,edge_attrs={'weight': [1]}


#Crear el grafo
#g = ig.Graph.Tree(127,2) #numero de vertices, mumero de hijos de cada vertice

#Codificar los vertices
# g = ig.Graph()
# g.add_vertices('Hola')
# g.vs[0]['name']='Hola'
# g.add_vertices('buenas')
# g.vs[1]['name']='buenas'
# g.add_edges([('Hola','buenas')])
# g['date'] = "2009"
# # print(g["date"]) #2009

# g.add_vertex('Hola')
# print(g)
# # print(g.vs[0].attributes()) #{'name': 'Hola'}
# print(g.degree(0)) #Grado del primer vertice
# g.get_vid()
