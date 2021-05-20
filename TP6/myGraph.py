# Graph implementation
from lib import algo1 as ALGO
from lib import linkedlist as LL
from lib import myarray as ARR
from lib import myqueue as Q
from lib.hashLinear import hashLinear as hashG

class Vertex:
    key = None
    neighborsList = None
    temp = None
    
def createGraph(vertexList, edgeList):
    '''
    Explanation: 
        Creates a graph from a given lists of vertex and edges.
    Info:
        Returns a simple graph, as a adjacency list.
    Params:
        vertexList: The list that contains the vertexes of the graph.
        edgeList: The list with the edges of each pair of vertex. 
    Return:
        The resultant graph.
    '''
    # Creates a graph object as an array of the size of vertexList
    graph = ALGO.Array(len(vertexList), Vertex())

    # Add each edge (pair of elements of edgeList) in the graph
    for i in range(0, len(edgeList), 2):
        # Check if each vertex already exists, otherwise, create it.
        vertex1 = graph[hashG(edgeList[i], graph)]
        if not vertex1:
            vertex1 = createVertex(edgeList[i])
            graph[hashG(vertex1.key, graph)] = vertex1

        vertex2 = graph[hashG(edgeList[i+1], graph)]
        if not vertex2:
            vertex2 = createVertex(edgeList[i+1])
            graph[hashG(vertex2.key, graph)] = vertex2

        # Adds each vertex as a neighbor of the other
        LL.add(vertex1.neighborsList, vertex2)
        LL.add(vertex2.neighborsList, vertex1)

    # Return the filled graph
    return graph

def existPath(graph, vertex1Key, vertex2Key):
    '''
    Descripción: Implementa la operación existe camino que busca si
        existe un camino entre los vértices v1 y v2
    Entrada: Grafo con la representación de Lista de Adyacencia, v1 y
        v2 vértices en el grafo.
    Salida: retorna True si existe camino entre v1 y v2, False en
        caso contrario.
    '''
    # Creates a variable to store and later return if a path exists between both vertex.
    existsPath = False

    # An additional list will be created to store each discovered node, to clear temps.
    discovered = Q.Queue()

    # Searches for the index of each vertex, can be None (not exists in the graph)
    vertex1Index = hashG(vertex1Key, graph)
    vertex2Index = hashG(vertex2Key, graph)

    # Check existence of the two vertexes after check for a path
    if (vertex1Index != None and vertex2Index != None) and (graph[vertex1Index] and graph[vertex2Index]):
        # Get pointers of the vertexes
        vertex1 = graph[vertex1Index]
        vertex2 = graph[vertex2Index]
        
        # Define the queue, set vertex1 as gray (BFS like)
        # ! Usage of temp attribute = None:WHITE, 0:GRAY, 1:BLACK
        queue = Q.Queue()
        vertex1.temp = 0
        Q.enqueue(queue, vertex1)
        Q.enqueue(discovered, vertex1)

        # Search until appears a path or empty queue
        while not existsPath and queue.tail:
            # Extract the actual vertex
            actualVertex = Q.dequeue(queue)

            # Discover new vertexes, set they as gray, and check for vertex2
            actualNeighbor = actualVertex.neighborsList.head
            while not existsPath and actualNeighbor:
                if actualNeighbor.value.temp == None:
                    # New vertex discover, check if is vertex2
                    if actualNeighbor.value is vertex2:
                        # Is vertex2! update existPath and break
                        existsPath = True
                        break
                    else:
                        # New node that is not vertex2, change to gray and enqueue
                        actualNeighbor.value.temp = 0
                        Q.enqueue(queue, actualNeighbor.value)
                        Q.enqueue(discovered, actualNeighbor.value)
                # Continue with the next neighbor
                actualNeighbor = actualNeighbor.nextNode
            
            # Set actual vertex to Black
            actualVertex.temp = 1

    # Clear temp values of discovered vertexes and return the result
    clearTemp(discovered)
    return existsPath

def isConnected(graph):
    '''
    Descripción: Implementa la operación es conexo
    Entrada: Grafo con la representación de Lista de Adyacencia.
    Salida: retorna True si existe camino entre todo par de vértices,
        False en caso contrario.
    '''

def createVertex(key):
    '''
    Creates and return a vertex object with the given key
    '''
    # Creates the vertex, assign the key and initialize list of neighbors
    newVertex = Vertex()
    newVertex.key = key
    newVertex.neighborsList = LL.LinkedList()

    # Return the pointer
    return newVertex

def clearTemp(listOfVertexes):
    '''
    Clears the temp value of a list of vertexes.
    '''
    while listOfVertexes.tail:
        actualVertex = Q.dequeue(listOfVertexes)
        actualVertex.temp = None

def printGraphAdjList(graph):
    '''
    Print an adjacency list simple graph
    '''
    for i in range(len(graph)):
        if graph[i]:
            print(f'[V: {graph[i].key}] -->', end=' ')
            actualNode = graph[i].neighborsList.head
            while actualNode:
                print(f'[{actualNode.value.key}]-', end='')
                actualNode = actualNode.nextNode
            print('')


###################################################
'''Test code'''


# Creates a simple graph using an adjacency list

vertex = [1, 3, 4, 5, 6, 8, 9, 12]
edges = [4, 5, 6, 3, 1, 8, 9, 12, 1, 3]

graph = createGraph(vertex, edges)
print('Graph ready')
printGraphAdjList(graph)

