from os import linesep, name
import igraph as ig
import cairo as cr

file = open("dataFollowers.txt",'r')
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

file = open("dataFriends.txt",'r')
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
#print(direcciones2)

direcciones = direcciones1 + direcciones2

def createGraph(listaDirecciones):
    #""""
    #INPUT:
    #   listaDirecciones: lista con los nodos y la direccion, p.ej [(pepe,pepa),(juan,jose)]
    #OUTPUT:
    #   grafo formado a partir de la lista
    #""""
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


    graph = ig.Graph(n=len(nodes), vertex_attrs = {'name':nodes}, directed= True, edges = edges)
    graph.es["weight"] = 1.0

    return graph, nodes




#ll = [('pepe','yo'),('yo','tu'),('ji','jo'),('yo','pepa'),('pepa','yo'),('pepa','pepita')] #REVISAR DIRECCIONES
gr , visited = createGraph(direcciones)
# print(gr)

#print(gr.es[0].attributes())


#gr.to_directed()

#print(gr)

"""         layouts           """
#layout = gr.layout('grid_fr')
layout= gr.layout_davidson_harel()
#layout= gr.layout_graphopt()
#layout= gr.layout_lgl()
#layout= gr.layout_reingold_tilford_circular()
#layout= gr.layout_sugiyama()

ig.plot(gr, layout = layout,target='myfile.png',bbox = (4000, 4000), margin = 20,vertex_label=visited)




#===TESTS===

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
