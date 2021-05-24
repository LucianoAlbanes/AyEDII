# Graph implementation
from lib import algo1 as ALGO
from lib import linkedlist as LL
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
        vertexList: A linked list that contains the vertexes of the graph.
        edgeList: A linked list with the edges of each pair of vertex. 
    Return:
        The resultant graph.
    '''
    # Creates a graph object as an array of the size of vertexList
    graph = ALGO.Array(LL.length(vertexList), Vertex())

    # Add each edge (pair of elements of edgeList) in the graph
    edgeNode = edgeList.head
    while edgeNode:
        # Store the key of each vertex
        key1 = edgeNode.value
        key2 = edgeNode.nextNode.value

        # Check if each vertex already exists, otherwise, create it.
        vertex1 = graph[hashG(key1, graph)]
        if not vertex1:
            vertex1 = createVertex(key1)
            graph[hashG(vertex1.key, graph)] = vertex1

        vertex2 = graph[hashG(key2, graph)]
        if not vertex2:
            vertex2 = createVertex(key2)
            graph[hashG(vertex2.key, graph)] = vertex2

        # Adds each vertex as a neighbor of the other
        LL.add(vertex1.neighborsList, vertex2)
        LL.add(vertex2.neighborsList, vertex1)

        # Increment by two nodes
        edgeNode = edgeNode.nextNode.nextNode

    # Return the filled graph
    return graph


def existPath(graph, vertex1Key, vertex2Key):
    '''
    Explanation: 
        Checks if exist a path between two vertexes.
    Params:
        graph: The graph (Adjacency list) to be searched.
        vertex1Key: A key that represents a vertex.
        vertex2Key: A key that represents a vertex. 
    Return:
        A boolean value, True if exists a path.
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
    Explanation: 
        Checks if there is a path between any pair of vertices of a given graph.
    Params:
        graph: The graph (Adjacency list) to be checked.
    Return:
        A boolean value, True if the graph is connected.
    '''
    # Creates a list to store all discovered vertexes
    discovered = Q.Queue()

    # Select an arbitrary vertex
    startVertex = graph[0]

    # Define the queue, set startVertex as gray (BFS like)
    # ! Usage of temp attribute = None:WHITE, 0:GRAY, 1:BLACK
    queue = Q.Queue()
    startVertex.temp = 0
    Q.enqueue(queue, startVertex)
    Q.enqueue(discovered, startVertex)

    # Discover all the graph
    while queue.tail:
        # Extract the actual vertex
        actualVertex = Q.dequeue(queue)

        # Discover new vertexes, set they as gray, and add to the discovered list
        actualNeighbor = actualVertex.neighborsList.head
        while actualNeighbor:
            if actualNeighbor.value.temp == None:
                # New vertex discover, change to gray and enqueue
                actualNeighbor.value.temp = 0
                Q.enqueue(queue, actualNeighbor.value)
                Q.enqueue(discovered, actualNeighbor.value)

            # Continue with the next neighbor
            actualNeighbor = actualNeighbor.nextNode

        # Set actual vertex to Black
        actualVertex.temp = 1

    # Call clearTemp to set temp to None. Additionally will return the number of discovered vertexes
    discoveredQuantity = clearTemp(discovered)

    # Return a boolean, True if the number of discovered vertexes equals to the quantity of vertexes in the graph
    return (discoveredQuantity == len(graph))


def isTree(graph):
    '''
    Explanation:
        Checks if a given graph is a tree.
    Params:
        graph: The graph (Adjacency list) to be checked.
    Return:
        A boolean value, True if the graph is a tree.
    '''
    # The graph is a tree until: 1. A cycle apears, or 2. Edges != Vertexes - 1 (See Theorem B.2 of CLRS)
    isTree = True

    # An additional list will be created to store each discovered node, to clear temps.
    discovered = Q.Queue()

    # Select an arbitrary vertex
    startVertex = graph[0]

    # Define the queue, set startVertex as gray (BFS like)
    # ! Usage of temp attribute = None:WHITE, 0:GRAY, 1:BLACK
    queue = Q.Queue()
    startVertex.temp = 0
    Q.enqueue(queue, (startVertex, None))  # Tuple, vertex and his parent
    Q.enqueue(discovered, startVertex)

    # Search until appears a path or empty queue
    while isTree and queue.tail:
        # Extract the actual vertex
        actualVertex, actualVertexParent = Q.dequeue(
            queue)  # Dequeue the tuple

        # Discover new vertexes, set they as gray, and check if a cycle apears
        actualNeighbor = actualVertex.neighborsList.head
        while isTree and actualNeighbor:
            if actualNeighbor.value.temp == None:
                # New vertex, change to gray and enqueue
                actualNeighbor.value.temp = 0
                # Enqueue with his parent vertex
                Q.enqueue(queue, (actualNeighbor.value, actualVertex))
                Q.enqueue(discovered, actualNeighbor.value)
            else:
                if not (actualNeighbor.value is actualVertexParent):
                    # A cycle apears!, actualNeighbor was discovered previously.
                    isTree = False
                    break

            # Continue with the next neighbor
            actualNeighbor = actualNeighbor.nextNode

        # Set actual vertex to Black
        actualVertex.temp = 1

    # Call clearTemp to set temp to None. Additionally will return the number of discovered vertexes
    discoveredQuantity = clearTemp(discovered)

    # Return a boolean.
    # Check if a cycle wasn't found and if is a connected graph
    return isTree and (discoveredQuantity == len(graph))


def createVertex(key):
    '''
    Explanation: 
        Creates a vertex with the given key, and return his pointer.
    '''
    # Creates the vertex, assign the key and initialize list of neighbors
    newVertex = Vertex()
    newVertex.key = key
    newVertex.neighborsList = LL.LinkedList()

    # Return the pointer
    return newVertex


def clearTemp(listOfVertexes):
    '''
    Explanation:
        Receives a list of vertexes, clears its temp value and returns the number of vertices cleared.
    '''
    count = 0
    while listOfVertexes.tail:
        actualVertex = Q.dequeue(listOfVertexes)
        actualVertex.temp = None
        count += 1
    return count


def printGraphAdjList(graph):
    '''
    Explanation:
        Prints an adjacency list simple graph.
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

vertex =  [1, 3, 4, 5, 6, 8, 9, 12]
edges =  [4, 5, 6, 3, 1, 8, 9, 12, 1, 3]


vertexList = LL.LinkedList()
edgesList = LL.LinkedList()

for element in vertex:
    LL.add(vertexList, element)

for element in edges:
    LL.add(edgesList, element)

graph = createGraph(vertexList, edgesList)
print('Graph ready')

printGraphAdjList(graph)
