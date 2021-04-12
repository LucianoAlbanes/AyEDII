# Binary tree ADT implementation.

from linkedlist import LinkedList, add

# Define classes.

class BinaryTree:
    root = None

class BinaryTreeNode:
    key = None
    value = None
    leftnode = None
    rightnode = None
    parent = None

# Define functions

def search(binaryTree, element):
    '''
    Explanation: 
        Searches for an element in the given binary tree.
    Params:
        binaryTree: The binary tree on which you want to perform the search.
        element: The element to search in the given binary tree.
    Return:
        The key of the node with the given element.
        If the element is found multiple times, returns the first key where appears. (Preorder)
        Returns 'None' if there is no a node with the given element in the binary tree.
    '''
    # Search recursively using aux fn, store pointer and return the key.
    foundNode = searchAux(binaryTree.root, element)
    if foundNode:
        return foundNode.key

def searchAux(actualNode, element):
    # Empty node case.
    if not actualNode:
        return None

    # Match case.
    if actualNode.value == element:
        return actualNode

    # Recursive part.
    # Search in both sides and store the return.
    foundNode = searchAux(actualNode.leftnode, element)
    if not foundNode:
        foundNode = searchAux(actualNode.rightnode, element)

    # Return the pointer of the node
    return foundNode

def insert(binaryTree, element, key):
    '''
    Explanation:
        Inserts an element with a given key in a binary tree.
    Params:
        binaryTree: The binary tree on which you want to perform the insert.
        element: The element to insert in the given binary tree.
        key: The key of the node with the given element to insert.
    Return:
        The key of the node of the inserted element.
        Returns 'None' if the insert cannot be performed (Exists a node with same key).
    '''
    # Check if the key already exists.
    if checkKeyExistence(binaryTree, key):
        return None

    # Create the new node
    newNode = BinaryTreeNode()
    newNode.key = key
    newNode.value = element

    # Case if empty tree.
    if not binaryTree.root:
        binaryTree.root = newNode
        return newNode.key

    # General case
    insertAux(binaryTree.root, newNode)
    return key

def insertAux(actualNode, newNode):
    # Left node case.
    if actualNode.key > newNode.key:
        if not actualNode.leftnode:
            actualNode.leftnode = newNode
            newNode.parent = actualNode
        else:
            insertAux(actualNode.leftnode, newNode)

    # Right node case.
    if actualNode.key < newNode.key:
        if not actualNode.rightnode:
            actualNode.rightnode = newNode
            newNode.parent = actualNode
        else:
            insertAux(actualNode.rightnode, newNode)

def delete(binaryTree, element):
    '''
    Explanation:
        Delete an node with a given element on an binary tree.
    Info:
        If exist more than one node with the element, only the first one will be deleted. (Preorder)
    Params:
        binaryTree: The binary tree on which you want to perform the delete.
        element: The element of the node of the binary tree to be deleted.
    Return:
        The key of the deleted node.
        Returns 'None' if there is no a node with the given element in the binary tree.
    '''
    # Search the element
    nodeToDelete = searchAux(binaryTree.root, element)

    # Not found case
    if not nodeToDelete:
        return None
    
    # Delete using aux fn
    deleteAux(binaryTree, nodeToDelete)

    # Return key
    return nodeToDelete.key

def deleteKey(binaryTree, key):
    '''
    Explanation:
        Delete an node with a given key on an binary tree.
    Params:
        binaryTree: The binary tree on which you want to perform the delete.
        key: The key of the node of the binary tree to be deleted.
    Return:
        The key of the deleted node.
        Returns 'None' if there is no a node with the given key.
    '''
    # Search the element
    nodeToDelete = checkKeyExistenceAux(binaryTree.root, key)

    # Not found case
    if not nodeToDelete:
        return None
    
    # Delete using aux fn
    deleteAux(binaryTree, nodeToDelete)

    # Return key
    return nodeToDelete.key

def deleteAux(binaryTree, nodeToDelete):
    # Caso nodo hoja
    if not (nodeToDelete.leftnode or nodeToDelete.rightnode):
        if nodeToDelete is nodeToDelete.parent.leftnode:
            nodeToDelete.parent.leftnode = None
        else:
            nodeToDelete.parent.rightnode = None
    # Caso sin rama izquierda
    elif not nodeToDelete.leftnode:
        moveNodes(binaryTree, nodeToDelete.rightnode, nodeToDelete)
    elif not nodeToDelete.rightnode: #Sin rama derecha
        moveNodes(binaryTree, nodeToDelete.leftnode, nodeToDelete)
    else: # ambas ramas
        # Define successor
        successorNode = nodeToDelete.rightnode
        while successorNode.leftnode:
            successorNode = successorNode.leftnode

        # Reasign pointers
        if successorNode.parent is nodeToDelete:
            if successorNode.rightnode:
                successorNode.rightnode.parent = successorNode
        else:
            moveNodes(binaryTree, successorNode.rightnode, successorNode)
            successorNode.rightnode = nodeToDelete.rightnode
            if successorNode.rightnode:
                successorNode.rightnode.parent = successorNode
        moveNodes(binaryTree, successorNode, nodeToDelete)
        successorNode.leftnode = nodeToDelete.leftnode
        successorNode.leftnode.parent = successorNode

def moveNodes(binaryTree, fromNode, toNode):
    '''
    la fn transplante o moveNodes coloca al nodo fromNode en la posicion del nodo toNode.
    Permite que fromNode sea un nodo nulo.
    No es responsable de la actualizacion de los hijos de ningun nodo
    '''
    if toNode is binaryTree.root: #Nodo viejo es raíz
        binaryTree.root = fromNode
    else: #Caso izq. o drch.
        if toNode == toNode.parent.leftnode:
            toNode.parent.leftnode = fromNode
        else:
            toNode.parent.rightnode = fromNode
    # Check si el nodo nuevo era nulo
    if fromNode:
        fromNode.parent = toNode.parent

def checkKeyExistence(binaryTree, key):
    '''
    Explanation: 
        Check if a given key exists on a binary tree.
    Params:
        binaryTree: The binary tree on which you want to perform the check.
        element: The key to search in the given binary tree.
    Return:
        The pointer of the node with the matching key, if exists.
        'False' otherwise
    '''
    # Case if empty tree.
    if not binaryTree.root:
        return False

    # Search recursively using aux fn, and return a boolean.
    return checkKeyExistenceAux(binaryTree.root, key)

def checkKeyExistenceAux(actualNode, key):
    # Empty node case.
    if not actualNode:
        return False

    # Match case.
    if actualNode.key == key:
        return actualNode

    # Recursive part.
    # Search in the side where could exist a same key.
    if key < actualNode.key:
        return checkKeyExistenceAux(actualNode.leftnode, key)
    else:
        return checkKeyExistenceAux(actualNode.rightnode, key)

def traverseInPreOrder(binaryTree):
    '''
    Explanation: 
        Create a linked list of the nodes of the binary tree in pre order.
    Params:
        binaryTree: The binary tree where are located the nodes to extract.
    Return:
        A linked list with the nodes in pre order.
        Returns 'None' if the tree is empty.
    '''
    # Empty tree case
    if not binaryTree.root:
        return None

    # Create the linked list to storage the pointers.
    nodesList = LinkedList()

    # Use an aux recursive fn to navigate the tree and store the pointers.
    traverseInPreOrderAux(binaryTree.root, nodesList)

    # Return the filled linked list.
    return nodesList

def traverseInPreOrderAux(actualNode, linkedList):
    # Recursively go to all nodes, both sides, right to left
    if actualNode.rightnode:
        traverseInPreOrderAux(actualNode.rightnode, linkedList)
    if actualNode.leftnode:
        traverseInPreOrderAux(actualNode.leftnode, linkedList)
        
    # Store the pointer in the linked list
    add(linkedList, actualNode)
