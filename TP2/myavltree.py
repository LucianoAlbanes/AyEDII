from mybinarytree import getNode, insertAux, searchAux, moveNode, search, access, update, traverseInPreOrder
# Define classes


class AVLTree:
    root = None


class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    balanceFactor = None
    height = None

# Define functions


def insert(avlTree, value, key):
    '''
    Explanation:
        Inserts an value with a given key in a AVL-Tree, rebalances itself.
    Params:
        avlTree: The AVL-Tree on which you want to perform the insert.
        value: The value to insert in the given binary tree.
        key: The key of the node with the given value to insert.
    Return:
        The key of the node of the inserted value.
        Returns 'None' if the insert cannot be performed (Exists a node with same key).
    '''
    # Check if the key already exists.
    if getNode(avlTree, key):
        return None

    # Create the new node
    newNode = AVLNode()
    newNode.key = key
    newNode.value = value

    # Insert node
    if not avlTree.root:  # Case if empty tree.
        avlTree.root = newNode
    else:  # General case
        insertAux(avlTree.root, newNode)

    # Update heights and bfs from the inserted node to the root
    updateHeight(newNode)
    updateBf(newNode, True)

    # Rebalance it
    reBalance(avlTree, newNode)

    # Return key of inserted node
    return key


def delete(avlTree, value):
    '''
    Explanation:
        Delete an node with a given value on an AVL-Tree, keeps balanced.
    Info:
        If exist more than one node with the value, only the first one will be deleted. (Preorder)
    Params:
        avlTree: The AVL-Tree on which you want to perform the delete.
        value: The value of the node of the tree to be deleted.
    Return:
        The key of the deleted node.
        Returns 'None' if there is no a node with the given value in the tree.
    '''
    # Search the value
    nodeToDelete = searchAux(avlTree.root, value)

    # Not found case
    if not nodeToDelete:
        return None

    # Only one node case
    if not (avlTree.root.leftnode or avlTree.root.rightnode):
        avlTree.root = None
        return nodeToDelete.key

    # Delete using aux fn, and store the rebalanceNode
    rebalanceNode = deleteAux(avlTree, nodeToDelete)
    if rebalanceNode.leftnode:
        # rebalance node can be a un balanced parent
        rebalanceNode = rebalanceNode.leftnode

    # Update heights and bfs from the rebalanceNode to the root
    updateHeight(rebalanceNode)
    updateBf(rebalanceNode, True)

    # Rebalance it from rebalanceNode
    reBalance(avlTree, rebalanceNode)

    # Return key
    return nodeToDelete.key


def deleteKey(avlTree, key):
    '''
    Explanation:
        Delete an node with a given key on an AVL-Tree, keeps balanced.
    Params:
        avlTree: The tree on which you want to perform the delete.
        key: The key of the node of the tree to be deleted.
    Return:
        The key of the deleted node.
        Returns 'None' if there is no a node with the given key.
    '''
    # Search the node
    nodeToDelete = getNode(avlTree, key)

    # Not found case
    if not nodeToDelete:
        return None

    # Only one node case
    if not (avlTree.root.leftnode or avlTree.root.rightnode):
        avlTree.root = None
        return nodeToDelete.key

    # Delete using aux fn, and store the rebalanceNode
    rebalanceNode = deleteAux(avlTree, nodeToDelete)

    # Update heights and bfs from the rebalanceNode to the root
    updateHeight(rebalanceNode)
    updateBf(rebalanceNode, True)

    # Rebalance it from rebalanceNode
    reBalance(avlTree, rebalanceNode)

    # Return key
    return nodeToDelete.key


def deleteAux(avlTree, nodeToDelete):
    # Store the pointer of the node to be used to rebalance, will be returned
    rebalanceNode = None

    # Deletetion algorithm
    # Case leaf node
    if not (nodeToDelete.leftnode or nodeToDelete.rightnode):
        rebalanceNode = nodeToDelete.parent
        if nodeToDelete is nodeToDelete.parent.leftnode:
            nodeToDelete.parent.leftnode = None
        else:
            nodeToDelete.parent.rightnode = None

    # Case right branch
    elif not nodeToDelete.leftnode:
        rebalanceNode = nodeToDelete.rightnode
        moveNode(avlTree, nodeToDelete.rightnode, nodeToDelete)

    # Case left branch
    elif not nodeToDelete.rightnode:
        rebalanceNode = nodeToDelete.leftnode
        moveNode(avlTree, nodeToDelete.leftnode, nodeToDelete)

    # Case both branchs
    else:
        # Define successor
        successorNode = nodeToDelete.rightnode
        while successorNode.leftnode:
            successorNode = successorNode.leftnode

        # Define rebalance node
        if successorNode.rightnode:
            rebalanceNode = successorNode.rightnode
        else:
            rebalanceNode = successorNode.parent

        # Reasign pointers
        if successorNode.parent is nodeToDelete:
            if successorNode.rightnode:
                successorNode.rightnode.parent = successorNode
        else:
            moveNode(avlTree, successorNode.rightnode, successorNode)
            successorNode.rightnode = nodeToDelete.rightnode
            if successorNode.rightnode:
                successorNode.rightnode.parent = successorNode
        moveNode(avlTree, successorNode, nodeToDelete)
        successorNode.leftnode = nodeToDelete.leftnode
        successorNode.leftnode.parent = successorNode

    # Return the rebalancer nodes
    if rebalanceNode.leftnode:
        # rebalance node can be an unbalanced parent
        rebalanceNode = rebalanceNode.leftnode
    return rebalanceNode


def rotateLeft(avlTree, avlNode):
    '''
    Explanation:
        The unbalanced avlNode becomes the child of its right child by performing a rotation.
    Params:
        avlTree: The AVL-Tree on which you want to perform the rotation.
        avlNode: The unbalanced avlNode 'root' to be rotated.
    Return:
        The pointer of the new balanced 'root' avlNode.
    '''
    # Check condition to rotate
    if not avlNode.rightnode:
        print("Can't rotate left, no rightnode")
    newRoot = avlNode.rightnode

    # Check if the new root have left child node
    if newRoot.leftnode:
        avlNode.rightnode = newRoot.leftnode
        avlNode.rightnode.parent = avlNode
    else:
        avlNode.rightnode = None

    # Change parents relationships betwen roots
    newRoot.parent = avlNode.parent
    if avlNode is avlTree.root:
        avlTree.root = newRoot
    else:
        if avlNode is avlNode.parent.rightnode:
            avlNode.parent.rightnode = newRoot
        else:
            avlNode.parent.leftnode = newRoot

    # Finish child's relationships
    newRoot.leftnode = avlNode
    avlNode.parent = newRoot

    # Fix heights
    updateHeight(newRoot.leftnode)

    # Return new root pointer
    return newRoot


def rotateRight(avlTree, avlNode):
    '''
    Explanation:
        The unbalanced avlNode becomes the child of its left child by performing a rotation.
    Params:
        avlTree: The AVL-Tree on which you want to perform the rotation.
        avlNode: The unbalanced avlNode 'root' to be rotated.
    Return:
        The pointer of the new balanced 'root' avlNode.
    '''
    # Check condition to rotate
    if not avlNode.leftnode:
        print("Can't rotate right, no leftnode")
    newRoot = avlNode.leftnode

    # Check if the new root have right child node
    if newRoot.rightnode:
        avlNode.leftnode = newRoot.rightnode
        avlNode.leftnode.parent = avlNode
    else:
        avlNode.leftnode = None

    # Change parents relationships betwen roots
    newRoot.parent = avlNode.parent
    if avlNode is avlTree.root:
        avlTree.root = newRoot
    else:
        if avlNode is avlNode.parent.leftnode:
            avlNode.parent.leftnode = newRoot
        else:
            avlNode.parent.rightnode = newRoot

    # Finish child's relationships
    newRoot.rightnode = avlNode
    avlNode.parent = newRoot

    # Fix heights
    updateHeight(newRoot.rightnode)

    # Return new root pointer
    return newRoot


def updateBf(avlNode, recursive):
    '''
    Explanation:
        Calculates and sets the balanceFactor parameter of an avlNode, and to the root of an AVL-Tree optionally.
    Params:
        avlNode: The node to update its balanceFactor.
        recursive: Boolean value, if want to continue recursively calculating bf until root.
    Info:
        This function DOESN'T UPDATE HEIGHTS, must be called updateHeight() first.
    '''
    # This recursive fn calcs and update the bf of avlNode, reading child's heights.
    # Store the height of each child nodes, if exists
    hightL = 0
    hightR = 0

    if avlNode.leftnode:
        hightL = avlNode.leftnode.height + 1
    if avlNode.rightnode:
        hightR = avlNode.rightnode.height + 1

    # Update the bf of the given node
    avlNode.balanceFactor = hightL - hightR

    # Calc new bf of his parent, until root
    if recursive and avlNode.parent:
        updateBf(avlNode.parent, True)


def updateHeight(avlNode):
    '''
    Explanation:
        Calculates and sets the height parameter from avlNode to the root of an AVL-Tree.
    Params:
        avlNode: The node to update its height, and its parents recursively.
    '''
    # Case both child nodes
    if avlNode.leftnode and avlNode.rightnode:
        if avlNode.leftnode.height > avlNode.rightnode.height:
            avlNode.height = 1 + avlNode.leftnode.height
        else:
            avlNode.height = 1 + avlNode.rightnode.height
    elif avlNode.leftnode:  # Only left child node
        avlNode.height = 1 + avlNode.leftnode.height
    elif avlNode.rightnode:  # Only right child node
        avlNode.height = 1 + avlNode.rightnode.height
    else:  # Leaf node
        avlNode.height = 0

    # Continue up if the avlNode isn't the tree's root
    if avlNode.parent:
        updateHeight(avlNode.parent)


def reBalance(avlTree, avlNode):
    '''
    Explanation:
        Checks and rebalance an AVL-Tree from avlNode to root.
    Params:
        avlTree: The AVL-Tree to be balanced.
        avlNode: The first node to be checked and rebalanced if is needed.
    Info:
        This function DOESN'T UPDATE BALANCE FACTORS, must be called updateBf() first.
    '''
    # Case inexistent node
    if not avlNode:
        return None

    # Check if is necessary to rebalance the node (bf != -1,0,1)
    if avlNode.balanceFactor < -1:  # unbalanced to the right
        if avlNode.rightnode.balanceFactor > 0:  # the rChild have rSubChild
            rotateRight(avlTree, avlNode.rightnode)
            rotateLeft(avlTree, avlNode)
        else:  # No rSubrChild
            rotateLeft(avlTree, avlNode)

        # Update balanceFactor of parent's right node ONLY, and from avlNode recursively to root.
        if avlNode.parent.rightnode:
            updateBf(avlNode.parent.rightnode, False)
        updateBf(avlNode, True)

    elif avlNode.balanceFactor > 1:  # unbalanced to the left
        if avlNode.leftnode.balanceFactor < 0:  # same reason
            rotateLeft(avlTree, avlNode.leftnode)
            rotateRight(avlTree, avlNode)
        else:
            rotateRight(avlTree, avlNode)

        # Update balanceFactor of parent's left node ONLY, and from avlNode recursively to root.
        if avlNode.parent.leftnode:
            updateBf(avlNode.parent.leftnode, False)
        updateBf(avlNode, True)
    else:
        # Continue recursively until root
        reBalance(avlTree, avlNode.parent)
