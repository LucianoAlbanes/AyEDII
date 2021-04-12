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
    foundNode = searchAux(binaryTree.root, element, None)
    if foundNode:
        return foundNode.key


def searchAux(actualNode, element, leafCheck):
    # Empty node case.
    if not actualNode:
        return None

    # Match case.
    if actualNode.value == element:
        if leafCheck:  # To use in the delete fn
            if actualNode.leftnode or actualNode.rightnode:
                return None
            else:
                return actualNode
        else:
            return actualNode

    # Recursive part.
    # Search in both sides and store the return.
    foundNode = searchAux(actualNode.leftnode, element, leafCheck)
    if not foundNode:
        foundNode = searchAux(actualNode.rightnode, element, leafCheck)

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
        Only can delete leaf nodes.
    Params:
        binaryTree: The binary tree on which you want to perform the delete.
        element: The element of the node of the binary tree to be deleted.
    Return:
        The key of the deleted node.
        Returns 'None' if there is no a node with the given element in the binary tree.
    '''
    # Search the element, with check leaf
    nodeToDelete = searchAux(binaryTree.root, element, True)

    # Unsuccessful case
    if not nodeToDelete:
        return None

    # Store the key of the node to delete
    key = nodeToDelete.key

    # Remove the node from the tree
    if nodeToDelete is nodeToDelete.parent.leftnode:
        nodeToDelete.parent.leftnode = None
    else:
        nodeToDelete.parent.rightnode = None

    # Return the key
    return key


def checkKeyExistence(binaryTree, key):
    '''
    Explanation: 
        Check if a given key exists on a binary tree.
    Params:
        binaryTree: The binary tree on which you want to perform the check.
        element: The key to search in the given binary tree.
    Return:
        A boolean value, indicating if a key exists in the binary tree.
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
        return True

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
