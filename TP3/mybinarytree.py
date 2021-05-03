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


def search(binaryTree, value):
    '''
    Explanation: 
        Searches for an value in the given binary tree.
    Params:
        binaryTree: The binary tree on which you want to perform the search.
        value: The value to search in the given binary tree.
    Return:
        The key of the node with the given value.
        If the value is found multiple times, returns the first key where appears. (Preorder)
        Returns 'None' if there is no a node with the given value in the binary tree.
    '''
    # Search recursively using aux fn, store pointer and return the key.
    foundNode = searchAux(binaryTree.root, value)
    if foundNode:
        return foundNode.key


def searchAux(actualNode, value):
    # Empty node case.
    if not actualNode:
        return None

    # Match case.
    if actualNode.value == value:
        return actualNode

    # Recursive part.
    # Search in both sides and store the return.
    foundNode = searchAux(actualNode.leftnode, value)
    if not foundNode:
        foundNode = searchAux(actualNode.rightnode, value)

    # Return the pointer of the node
    return foundNode


def insert(binaryTree, value, key):
    '''
    Explanation:
        Inserts an value with a given key in a binary tree.
    Params:
        binaryTree: The binary tree on which you want to perform the insert.
        value: The value to insert in the given binary tree.
        key: The key of the node with the given value to insert.
    Return:
        The key of the node of the inserted value.
        Returns 'None' if the insert cannot be performed (Exists a node with same key).
    '''
    # Check if the key already exists.
    if getNode(binaryTree, key):
        return None

    # Create the new node
    newNode = BinaryTreeNode()
    newNode.key = key
    newNode.value = value

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


def delete(binaryTree, value):
    '''
    Explanation:
        Delete an node with a given value on an binary tree.
    Info:
        If exist more than one node with the value, only the first one will be deleted. (Preorder)
    Params:
        binaryTree: The binary tree on which you want to perform the delete.
        value: The value of the node of the binary tree to be deleted.
    Return:
        The key of the deleted node.
        Returns 'None' if there is no a node with the given value in the binary tree.
    '''
    # Search the value
    nodeToDelete = searchAux(binaryTree.root, value)

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
    # Search the value
    nodeToDelete = getNodeAux(binaryTree.root, key)

    # Not found case
    if not nodeToDelete:
        return None

    # Delete using aux fn
    deleteAux(binaryTree, nodeToDelete)

    # Return key
    return nodeToDelete.key


def deleteAux(binaryTree, nodeToDelete):
    # Case leaf node
    if not (nodeToDelete.leftnode or nodeToDelete.rightnode):
        if nodeToDelete is nodeToDelete.parent.leftnode:
            nodeToDelete.parent.leftnode = None
        else:
            nodeToDelete.parent.rightnode = None

    # Case right branch
    elif not nodeToDelete.leftnode:
        moveNode(binaryTree, nodeToDelete.rightnode, nodeToDelete)

    # Case left branch
    elif not nodeToDelete.rightnode:
        moveNode(binaryTree, nodeToDelete.leftnode, nodeToDelete)

    # Case both branchs
    else:
        # Define successor
        successorNode = nodeToDelete.rightnode
        while successorNode.leftnode:
            successorNode = successorNode.leftnode

        # Reasign pointers
        if successorNode.parent is nodeToDelete:
            if successorNode.rightnode:
                successorNode.rightnode.parent = successorNode
        else:
            moveNode(binaryTree, successorNode.rightnode, successorNode)
            successorNode.rightnode = nodeToDelete.rightnode
            if successorNode.rightnode:
                successorNode.rightnode.parent = successorNode
        moveNode(binaryTree, successorNode, nodeToDelete)
        successorNode.leftnode = nodeToDelete.leftnode
        successorNode.leftnode.parent = successorNode


def moveNode(binaryTree, fromNode, toNode):
    '''
    Explanation: 
        Overwrite the pointer of one node by another, inside the binary tree.
    Params:
        binaryTree: The binary tree on which you want to perform the operation.
        fromNode: The node to be moved over the location of the another.
        toNode: The node to be overwrite by the 'fromNode'
    '''
    if toNode is binaryTree.root:  # Nodo viejo es raíz
        binaryTree.root = fromNode
    else:  # Caso izq. o drch.
        if toNode == toNode.parent.leftnode:
            toNode.parent.leftnode = fromNode
        else:
            toNode.parent.rightnode = fromNode
    # Check si el nodo nuevo era nulo
    if fromNode:
        fromNode.parent = toNode.parent
    else:
        toNode.parent = None


def getNode(binaryTree, key):
    '''
    Explanation: 
        Get the pointer of a node with the given key
    Params:
        binaryTree: The binary tree on which you want to perform the operation.
        value: The key to search in the given binary tree.
    Return:
        The pointer of the node with the matching key, if exists.
        Otherwise 'None'
    '''
    # Case if empty tree.
    if not binaryTree.root:
        return None

    # Search recursively using aux fn, and return the pointer
    return getNodeAux(binaryTree.root, key)


def getNodeAux(actualNode, key):
    # Empty node case.
    if not actualNode:
        return None

    # Match case.
    if actualNode.key == key:
        return actualNode

    # Recursive part.
    # Search in the side where could exist a same key.
    if key < actualNode.key:
        return getNodeAux(actualNode.leftnode, key)
    else:
        return getNodeAux(actualNode.rightnode, key)


def access(binaryTree, key):
    '''
    Explanation: 
        Access to an value in the given key of the binary tree.
    Params:
        binaryTree: The binary tree on which you want to perform the access.
        key: The key of the node of the binary tree to be accessed.
    Return:
        The value of the value with the given key.
        Returns 'None' if the key does not exist in the binary tree.
    '''
    node = getNodeAux(binaryTree.root, key)
    if node:
        return node.value
    return None


def update(binaryTree, value, key):
    '''
    Explanation: 
        Update the value of a node with the given key.
    Params:
        binaryTree: The binary tree where is located the node to update.
        value: The new value of the node to update in the binary tree.
        key: The key of the node of the binary tree to be updated.
    Return:
        The key of the updated node.
        Returns 'None' if there is no node with the given key.
    '''
    nodeToUpdate = getNodeAux(binaryTree.root, key)

    # Not found case
    if not nodeToUpdate:
        return None

    # Change value and return key
    nodeToUpdate.value = value
    return nodeToUpdate.key


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
