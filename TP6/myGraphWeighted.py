# Weighted Graph (Adjacency matrix) implementation
from lib import algo1 as ALGO
from lib import linkedlist as LL
from lib import myqueue as Q
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
        Returns a weighted graph, as a adjacency matrix.
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
    '''
    Explanation: 
        Creates an minimun spanning tree from a graph.
    Params:
        graph: The graph (Adjacency matrix) to be used to create the MST.
    Return:
        A new graph, with the same vertexes but as an minimun spanning tree.
        If the given graph is not conencted, will return 'None'.
    '''
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
                # verify that actualVertex has not been discovered.
                if not graph[i].temp:
                    actualWeight = actualVertex.value.data[i]
                    if actualWeight and (minWeight is None or minWeight > actualWeight):
                        # Apears an edge with less weight.
                        minWeight = actualWeight
                        vertex1Key = actualVertex.value.key
                        vertex2Key = graph[i].key
            actualVertex = actualVertex.nextNode

        # Verify if a new edge was discovered, else the graph is not connected
        if not minWeight:
            print('This graph is not connected. Make a MST is not possible.')
            break

        # Set the new edge as discovered, increment discoverdN, and add it to the lists to make a mstGraph.
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


def makeTree(graph):
    '''
    Explanation: 
        Creates a MST from a given graph.
    Info:
        This function is restricted to work with vertexes of weight = 1.
        Will discover the tree using BFS.
    Params:
        graph: The graph (Adjacency matrix) to be used.
    Return:
        A new graph, with the same vertexes but as an minimun spanning tree.
        If the given graph is not conencted or exists a edge with weight != 1, will return 'None'. 
    '''
    # Create three LList with the vertexes, edges and weights of the MST
    mstVertexes = LL.LinkedList()
    mstEdges = LL.LinkedList()
    mstWeights = LL.LinkedList()

    # Define the queue, set graph[0] as discovered (BFS like)
    # ! Usage of temp attribute = True if vertex was discovered
    queue = Q.Queue()
    graph[0].temp = True
    Q.enqueue(queue, 0)
    LL.add(mstVertexes, graph[0].key)

    # Search until empty queue
    RWeightFlag = True  # To verify the restriction weight = 1
    while RWeightFlag and queue.tail:
        # Extract the actual vertex index
        actualVertexIndex = Q.dequeue(queue)

        # Discover new vertexes, set they as discovered, and check if weight = 1
        for i in range(len(graph)):
            actualWeight = graph[actualVertexIndex].data[i]
            if actualWeight == 1 and not graph[i].temp:
                # New vertex, change to discovered and enqueue
                graph[i].temp = True

                # Enqueue
                Q.enqueue(queue, i)

                # Add this pair of vertexes to the MST lists
                LL.add(mstVertexes, graph[i].key)
                LL.add(mstEdges, graph[i].key)
                LL.add(mstEdges, graph[actualVertexIndex].key)
                LL.add(mstWeights, actualWeight)

            elif actualWeight and actualWeight != 1:
                # Check restriction, M[u,v]=1 if (u,v)∈ A
                RWeightFlag = False
                print(
                    f'This graph does not satisfy M[u,v]=1 if (u,v)∈A | M[{graph[i].key}, {graph[actualVertexIndex].key}]={actualWeight}')
                break

    # Clear temps and store the quantity of cleared (and discovered) vertexes
    qDiscoveredVertexes = clearTemp(graph, mstVertexes)

    # Verify if the graph is connected and make the new MST Graph
    mstGraph = None
    if RWeightFlag and qDiscoveredVertexes == len(graph):
        mstGraph = createGraph(mstVertexes, mstEdges, mstWeights)

    # Return the new graph
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


def clearTemp(graph, listOfVertexes):
    '''
    Explanation:
        Receives a list of vertexes index and a graph, clears its temp value and returns the number of vertexes cleared.
    '''
    count = 0
    actualVertex = listOfVertexes.head
    while actualVertex:
        graph[hashG(actualVertex.value, graph)].temp = None
        actualVertex = actualVertex.nextNode
        count += 1
    return count


###################################################
'''Test code'''


# Creates a weighted graph as a adjacency matrix
# The following graph was extracted from the slides of ”Árboles Abarcadores” (https://ibb.co/261MmYK)
vertex = [1, 2, 3, 4, 5, 6]
edges = [1, 4, 1, 2, 1, 3, 2, 3, 4, 3, 3, 5, 3, 6, 5, 6, 2, 5, 4, 6]
weights = [5, 6, 1, 5, 5, 6, 4, 6, 3, 2]
weights2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

vertexList = LL.LinkedList()
edgesList = LL.LinkedList()
weightsList = LL.LinkedList()
weights2List = LL.LinkedList()

for element in vertex:
    LL.add(vertexList, element)

for element in edges:
    LL.add(edgesList, element)

for element in weights:
    LL.add(weightsList, element)
for element in weights2:
    LL.add(weights2List, element)

# Create graph
graph = createGraph(vertexList, edgesList, weightsList)
print('Graph ready')
printGraphAdjMatrix(graph)

print('\n\nGraph MST\n')
printGraphAdjMatrix(primMST(graph))

# Create another graph, but with 1 as weights
print('\n\nGraph MST (Weight = 1)\n')
graph2 = createGraph(vertexList, edgesList, weights2List)
printGraphAdjMatrix(makeTree(graph2))
