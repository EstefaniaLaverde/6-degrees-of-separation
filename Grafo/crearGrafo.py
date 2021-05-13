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

direcciones = [] #LISTA CON LAS DIRECCIONES DE LOS FOLLOWERS
for lista in listUsers:
    centralNode = lista[0]
    lista.remove(centralNode)
    for user in lista:
        direcciones.append((centralNode,user))

file.close()

file = open("dataFriends.txt",'r')
fLines = file.readlines()

listUsers = []
# for line in flines:
#     if line[]

def createGraph(listaDirecciones):
    #""""
    #INPUT: 
    #   listaDirecciones: lista con los nodos y la direccion, p.ej [(pepe,pepa),(juan,jose)]
    #OUTPUT:
    #   grafo formado a partir de la lista
    #""""
    index = 0
    visited = []
    principalNodes = [] #Para guardar los colores 
    graph = ig.Graph()

    for direction in listaDirecciones:
        culito = direction[0]
        cabeza = direction[1]
        if culito not in principalNodes:
            principalNodes.append(culito)
        if culito in visited:
                
            if cabeza not in visited:
                visited.append(cabeza)
                graph.add_vertices(1)
                graph.vs[index]['name'] = cabeza
                graph.vs[index]['principal'] = culito
                graph.add_edges([(culito,cabeza)])
                index+=1

            elif cabeza in visited:
                n1 = graph.vs.find(name=culito).index
                n2 = graph.vs.find(name=cabeza).index
                # print(culito,n1)
                graph.add_edges([(n1,n2)])

        elif culito not in visited:
            if cabeza in visited:
                visited.append(culito)
                graph.add_vertices(1)
                graph.vs[index]['name'] = culito
                graph.vs[index]['principal'] = culito
                graph.add_edges([(culito,cabeza)])
                index+=1
            
            elif cabeza not in visited:
                visited.append(culito)
                graph.add_vertices(1)
                graph.vs[index]['name'] = culito
                graph.vs[index]['principal'] = culito
                index+=1

                visited.append(cabeza)
                graph.add_vertices(1)
                graph.vs[index]['name'] = cabeza
                graph.vs[index]['principal'] = culito
                index+=1

                graph.add_edges([(culito,cabeza)])
    return graph, principalNodes

ll = [('pepe','yo'),('yo','tu'),('ji','jo'),('yo','pepa'),('pepa','yo'),('pepa','pepita')] #REVISAR DIRECCIONES
gr , principalNodes= createGraph(direcciones)
# print(gr)



layout = gr.layout('grid_fr')
ig.plot(gr, layout = layout,target='myfile.png',bbox = (1000, 1000), margin = 20)

#===TESTS===

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
