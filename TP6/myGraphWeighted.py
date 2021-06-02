# Weighted Graph (Adjacency matrix) implementation
from lib.tree import Tree
from lib import algo1 as ALGO
from lib import linkedlist as LL
from lib.hashLinear import hashLinear as hashG


class Vertex:
    key = None
    data = None
    temp = None


def createGraph(vertexList, edgeList, weightList):
    '''
    Explanation: 
        Creates a graph from a given lists of vertex and edges.
    Info:
        Returns a simple graph, as a adjacency matrix.
    Params:
        vertexList: A linked list that contains the vertexes of the graph.
        edgeList: A linked list with the edges of each pair of vertex.
        weightList: A linked list with the weight of each pair of values of edgeList.
    Return:
        The resultant graph.
    '''
    # Creates a matrix of size vertexQuantity², store integers
    vertexQuantity = LL.length(vertexList)
    graph = ALGO.Array(vertexQuantity, Vertex())

    # Initialize each vertex
    actualVertex = vertexList.head
    while actualVertex:
        graph[hashG(actualVertex.value, graph)
              ] = createVertex(actualVertex.value, vertexQuantity)
        actualVertex = actualVertex.nextNode

    # Add each edge (pair of elements of edgeList) in the graph, with their respective weight
    actualEdges = edgeList.head
    actualWeight = weightList.head
    while actualEdges:
        # Store the index of each vertex.
        index1 = hashG(actualEdges.value, graph)
        index2 = hashG(actualEdges.nextNode.value, graph)

        # Change the value to 1, (representing an edge)
        graph[index1].data[index2] = actualWeight.value
        graph[index2].data[index1] = actualWeight.value

        # Increment both linked lists
        actualEdges = actualEdges.nextNode.nextNode
        actualWeight = actualWeight.nextNode

    # Return the filled graph
    return graph


def createVertex(key, lengthOfArray):
    '''
    Explanation: 
        Creates a vertex of a Matrix graph with the given key, and return his pointer.
    '''
    # Creates the vertex, assign the key and initialize list of neighbors
    newVertex = Vertex()
    newVertex.key = key
    newVertex.data = ALGO.Array(lengthOfArray, 0)

    # Return the pointer
    return newVertex


def primMST(graph):
    # minimum spanning tree (MST)
    # Select an arbitrary vertex as root, add it into a LList of discovered vertexes.
    # Each vertex in that list was discovered and is part of the spanning tree (|U| set s/ CLRS).
    # To improve time efficiency, a temp attribute will be used in each vertex to mark it as discovered or not.
    graph[0].temp = True
    discovered = LL.LinkedList()
    LL.add(discovered, graph[0])

    # Create two LList with the edges and weights of the MST
    mstEdges = LL.LinkedList()
    mstWeights = LL.LinkedList()

    # Search with the PRIM algorithm
    discoveredN = 1
    while discoveredN != len(graph):
        vertex1Key = None
        vertex2Key = None
        minWeight = None

        # Search for the minimum weight
        actualVertex = discovered.head
        while actualVertex:
            for i in range(len(graph)):
                actualWeight = actualVertex.value.data[i]
                # graph[i].temp to verify that vertex has not been discovered.
                if actualWeight and (minWeight is None or minWeight > actualWeight) and not graph[i].temp:
                    # Apears an edge with less weight.
                    minWeight = actualWeight
                    vertex1Key = actualVertex.value.key
                    vertex2Key = graph[i].key
            actualVertex = actualVertex.nextNode

        # Verify if a new edge was discovered, else the graph is not connected
        if not minWeight:
            print('This graph is not connected. Make a MST is not possible.')
            break

        # Set the new edge as discovered, increment discoverdN, and add it as mstEdges
        graph[vertex2Key].temp = True
        discoveredN += 1
        LL.add(discovered, graph[vertex2Key])
        LL.add(mstEdges, vertex1Key)
        LL.add(mstEdges, vertex2Key)
        LL.add(mstWeights, minWeight)

    # Create the new graph as a MST (if the while wasn't broken)
    mstGraph = None
    if minWeight:
        # Create a linked list with the vertexes values
        mstVertexes = LL.LinkedList()
        for i in range(len(graph)):
            LL.add(mstVertexes, graph[i].key)

        # Create the new graph as MST
        mstGraph = createGraph(mstVertexes, mstEdges, mstWeights)

    # Clear temp values of the discovered nodes
    actualNode = discovered.head
    while actualNode:
        actualNode.value.temp = None
        actualNode = actualNode.nextNode
    
    # Return the MST
    return mstGraph


def printGraphAdjMatrix(graph):
    '''
    Explanation:
        Prints an adjacency matrix graph.
    '''
    def replaceNone(data):
        result = 0
        if data != None:
            result = (f'\033[91m{data}\033[0m')  # 🌈🌈🌈 dye it
        return result

    # Print first row
    print(f'    [{graph[0].key}, ', end='')
    for i in range(1, len(graph)-1):
        print(f'{graph[i].key}, ', end='')
    print(f'{graph[len(graph)-1].key}]')

    # Content of the matrix
    for i in range(len(graph)):
        if graph[i]:
            # First column
            print(f'[{graph[i].key}]', end='|')

            # [i].data
            print(f'[{replaceNone(graph[i].data[0])}, ', end='')
            for j in range(1, len(graph)-1):
                print(f'{replaceNone(graph[i].data[j])}, ', end='')
            print(f'{replaceNone(graph[i].data[len(graph)-1])}]')


###################################################
'''Test code'''


# Creates a weighted graph as a adjacency matrix
# The following graph was extracted from Gaby's video (https://ibb.co/261MmYK)
vertex = [1, 2, 3, 4, 5, 6]
edges = [1, 4, 1, 2, 1, 3, 2, 3, 4, 3, 3, 5, 3, 6, 5, 6, 2, 5, 4, 6]
weights = [5, 6, 1, 5, 5, 6, 4, 6, 3, 2]

vertexList = LL.LinkedList()
edgesList = LL.LinkedList()
weightsList = LL.LinkedList()

for element in vertex:
    LL.add(vertexList, element)

for element in edges:
    LL.add(edgesList, element)

for element in weights:
    LL.add(weightsList, element)

# Create graph
graph = createGraph(vertexList, edgesList, weightsList)
print('Graph ready')
printGraphAdjMatrix(graph)

print('\n\nGraph MST\n')
printGraphAdjMatrix(primMST(graph))
