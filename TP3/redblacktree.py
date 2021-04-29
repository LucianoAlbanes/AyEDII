# Red-Black Tree implementation
from mybinarytree import getNode, insertAux, searchAux, moveNode, search, access, update, traverseInPreOrder

# Define classes


class RedBlackTree:
    root = None


class RedBlackNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    red = None
    value = None


nilNode = RedBlackNode()
# Define functions


def insert(RBTree, value, key):
    '''
    Explanation:
        Inserts an value with a given key in a Red-Black Tree, fix violations.
    Params:
        RBTree: The Red-Black Tree on which you want to perform the insert.
        value: The value to insert in the given binary tree.
        key: The key of the node with the given value to insert.
    Return:
        The key of the node of the inserted value.
        Returns 'None' if the insert cannot be performed (Exists a node with same key).
    '''
    # Check if the key already exists.
    if getNode(RBTree, key):
        return None

    # Create the new node
    newNode = RedBlackNode()
    newNode.key = key
    newNode.red = True
    newNode.value = value

    # Insert node
    if not RBTree.root:  # Case if empty tree.
        RBTree.root = newNode
    else:  # General case
        insertAux(RBTree.root, newNode)

    # Fix RBTree inconssistences.
    fixup(RBTree, newNode)

    # Return key of inserted node
    return key


def fixup(RBTree, RBNode):
    '''
    Explanation:
        Correct all possible RBNode violations according to the Red-Black tree specification.
    Params:
        RBTree: The Red-Black Tree on which you want to perform the operation.
        RBNode: The RBNode to check if violations exists.
    '''
    while RBNode.parent and RBNode.parent.parent and RBNode.parent.red:
        if RBNode.parent is RBNode.parent.parent.leftnode:
            uncle = RBNode.parent.parent.rightnode
            if uncle and uncle.red:
                RBNode.parent.red = False  # Case 1
                uncle.red = False  # Case 1
                RBNode.parent.parent.red = True  # Case 1
                RBNode = RBNode.parent.parent
            else:
                if RBNode is RBNode.parent.rightnode:
                    RBNode = RBNode.parent  # Case 2
                    rotateLeft(RBTree, RBNode)  # Case 2
                RBNode.parent.red = False  # Case 3
                RBNode.parent.parent.red = True  # Case 3
                rotateRight(RBTree, RBNode.parent.parent)  # Case 3
        else:
            uncle = RBNode.parent.parent.leftnode
            if uncle and uncle.red:
                RBNode.parent.red = False  # Case 1
                uncle.red = False  # Case 1
                RBNode.parent.parent.red = True  # Case 1
                RBNode = RBNode.parent.parent
            else:
                if RBNode is RBNode.parent.leftnode:
                    RBNode = RBNode.parent  # Case 2
                    rotateRight(RBTree, RBNode)  # Case 2
                RBNode.parent.red = False  # Case 3
                RBNode.parent.parent.red = True  # Case 3
                rotateLeft(RBTree, RBNode.parent.parent)  # Case 3
    RBTree.root.red = False


def rotateLeft(RBTree, RBNode):
    '''
    Explanation:
        The unbalanced RBNode becomes the child of its right child by performing a rotation.
    Params:
        RBTree: The Red-Black Tree on which you want to perform the rotation.
        RBNode: The unbalanced RBNode 'root' to be rotated.
    Return:
        The pointer of the new balanced 'root' RBNode.
    '''
    # Check condition to rotate
    if not RBNode.rightnode:
        print("Can't rotate left, no rightnode")
    newRoot = RBNode.rightnode

    # Check if the new root have left child node
    if newRoot.leftnode:
        RBNode.rightnode = newRoot.leftnode
        RBNode.rightnode.parent = RBNode
    else:
        RBNode.rightnode = None

    # Change parents relationships betwen roots
    newRoot.parent = RBNode.parent
    if RBNode is RBTree.root:
        RBTree.root = newRoot
    else:
        if RBNode is RBNode.parent.rightnode:
            RBNode.parent.rightnode = newRoot
        else:
            RBNode.parent.leftnode = newRoot

    # Finish child's relationships
    newRoot.leftnode = RBNode
    RBNode.parent = newRoot

    # Return new root pointer
    return newRoot


def rotateRight(RBTree, RBNode):
    '''
    Explanation:
        The unbalanced RBNode becomes the child of its left child by performing a rotation.
    Params:
        RBTree: The Red-Black Tree on which you want to perform the rotation.
        RBNode: The unbalanced RBNode 'root' to be rotated.
    Return:
        The pointer of the new balanced 'root' RBNode.
    '''
    # Check condition to rotate
    if not RBNode.leftnode:
        print("Can't rotate right, no leftnode")
    newRoot = RBNode.leftnode

    # Check if the new root have right child node
    if newRoot.rightnode:
        RBNode.leftnode = newRoot.rightnode
        RBNode.leftnode.parent = RBNode
    else:
        RBNode.leftnode = None

    # Change parents relationships betwen roots
    newRoot.parent = RBNode.parent
    if RBNode is RBTree.root:
        RBTree.root = newRoot
    else:
        if RBNode is RBNode.parent.leftnode:
            RBNode.parent.leftnode = newRoot
        else:
            RBNode.parent.rightnode = newRoot

    # Finish child's relationships
    newRoot.rightnode = RBNode
    RBNode.parent = newRoot

    # Return new root pointer
    return newRoot


def delete(RBTree, value):
    '''
    Explanation:
        Delete an node with a given value on an Red-Black Tree, fix violations.
    Info:
        If exist more than one node with the value, only the first one will be deleted. (Preorder)
    Params:
        RBTree: The Red-Black Tree on which you want to perform the delete.
        value: The value of the node of the tree to be deleted.
    Return:
        The key of the deleted node.
        Returns 'None' if there is no a node with the given value in the tree.
    '''
    # Search the value
    nodeToDelete = searchAux(RBTree.root, value)

    # Not found case
    if not nodeToDelete:
        return None

    # Only one node case
    if not (RBTree.root.leftnode or RBTree.root.rightnode):
        RBTree.root = None
        return nodeToDelete.key

    # Delete using aux fn
    deleteAux(RBTree, nodeToDelete)

    # Unlink nilNode from the tree
    removeTempNode()

    # Return key
    return nodeToDelete.key


def deleteKey(RBTree, key):
    '''
    Explanation:
        Delete an node with a given key on an Red-Black Tree,  fix violations.
    Params:
        RBTree: The tree on which you want to perform the delete.
        key: The key of the node of the tree to be deleted.
    Return:
        The key of the deleted node.
        Returns 'None' if there is no a node with the given key.
    '''
    # Search the value
    nodeToDelete = getNode(RBTree, key)

    # Not found case
    if not nodeToDelete:
        return None

    # Only one node case
    if not (RBTree.root.leftnode or RBTree.root.rightnode):
        RBTree.root = None
        return nodeToDelete.key

    # Delete using aux fn
    deleteAux(RBTree, nodeToDelete)

    # Unlink nilNode from the tree
    removeTempNode()

    # Return key
    return nodeToDelete.key


def deleteAux(RBTree, RBNode):
    '''
    Perform the deletion of the RBNode,
    and prepares the tree for the deleteFixup() that will be called inside.
    '''
    successorNode = RBNode
    successorColor = successorNode.red
    fixupNode = None

    # Case leaf node
    if not (RBNode.leftnode or RBNode.rightnode):
        if RBNode is RBNode.parent.leftnode:
            if RBNode.red:
                RBNode.parent.leftnode = None
            else:
                RBNode.parent.leftnode = createTempNode(RBNode.parent, True)
                fixupNode = RBNode.parent.leftnode
        else:
            if RBNode.red:
                RBNode.parent.rightnode = None
            else:
                RBNode.parent.rightnode = createTempNode(RBNode.parent, False)
                fixupNode = RBNode.parent.rightnode

    # Case right branch
    elif not RBNode.leftnode:
        fixupNode = RBNode.rightnode
        moveNode(RBTree, RBNode.rightnode, RBNode)

    # Case left branch
    elif not RBNode.rightnode:
        fixupNode = RBNode.leftnode
        moveNode(RBTree, RBNode.leftnode, RBNode)

    # Case both branches
    else:
        # Define successorNode
        successorNode = RBNode.rightnode
        while successorNode.leftnode:
            successorNode = successorNode.leftnode

        successorColor = successorNode.red
        fixupNode = successorNode.rightnode
        if not fixupNode:
            if successorNode.parent.rightnode is successorNode:
                fixupNode = createTempNode(successorNode.parent, False)
            else:
                fixupNode = createTempNode(successorNode.parent, True)

        # Reasign pointers
        if successorNode.parent is RBNode:
            if fixupNode:
                fixupNode.parent = successorNode
        else:
            if successorNode.rightnode:
                moveNode(RBTree, successorNode.rightnode, successorNode)
            successorNode.rightnode = RBNode.rightnode
            if successorNode.rightnode:
                successorNode.rightnode.parent = successorNode
        moveNode(RBTree, successorNode, RBNode)
        successorNode.leftnode = RBNode.leftnode
        successorNode.leftnode.parent = successorNode
        successorNode.red = RBNode.red

    # Call fixup fn if necessary
    if not successorColor:
        deleteFixup(RBTree, fixupNode)


def deleteFixup(RBTree, RBNode):
    '''
    This function fix the possibles violations from the RBNode.
    '''
    # CLRS <3
    while RBNode.parent and not RBNode.red:
        if RBNode is RBNode.parent.leftnode:  # RBNode is leftnode case
            siblingNode = RBNode.parent.rightnode
            if isRed(siblingNode):  # Case 1
                siblingNode.red = False
                RBNode.parent.red = True
                rotateLeft(RBTree, RBNode.parent)
                siblingNode = RBNode.parent.rightnode

            if not (isRed(siblingNode.leftnode) or isRed(siblingNode.rightnode)):
                siblingNode.red = True
                RBNode = RBNode.parent
            else:
                if not isRed(siblingNode.rightnode):  # Case 3
                    siblingNode.leftnode.red = False
                    siblingNode.red = True
                    rotateRight(RBTree, siblingNode)
                    siblingNode = RBNode.parent.rightnode
                siblingNode.red = RBNode.parent.red  # Case 4
                RBNode.parent.red = False
                siblingNode.rightnode.red = False
                rotateLeft(RBTree, RBNode.parent)
                RBNode = RBTree.root
        else:  # RBNode is rightnode case
            siblingNode = RBNode.parent.leftnode
            if siblingNode.red:  # Case 1
                siblingNode.red = False
                RBNode.parent.red = True
                rotateRight(RBTree, RBNode.parent)
                siblingNode = RBNode.parent.leftnode

            if not (isRed(siblingNode.leftnode) or isRed(siblingNode.rightnode)):  # Case 2
                siblingNode.red = True
                RBNode = RBNode.parent
            else:
                if not isRed(siblingNode.leftnode):  # Case 3
                    siblingNode.rightnode.red = False
                    siblingNode.red = True
                    rotateLeft(RBTree, siblingNode)
                    siblingNode = RBNode.parent.leftnode
                siblingNode.red = RBNode.parent.red  # Case 4
                RBNode.parent.red = False
                siblingNode.leftnode.red = False
                rotateRight(RBTree, RBNode.parent)
                RBNode = RBTree.root
    RBNode.red = False


def isRed(RBNode):
    '''
    Return the color of RBNode (handles NULL Nodes)
    '''
    if RBNode:
        return RBNode.red
    else:
        return False  # non-existant node = Black


def createTempNode(parent, isLeftChild):
    '''
    Creates a temp 'Nil Node' (Like CLRS), useful in some cases of the deletion.
    Will be removed after perform the deletion
    nilNode object is global.
    '''
    nilNode.parent = parent
    nilNode.red = False
    if isLeftChild:
        parent.leftnode = nilNode
    else:
        parent.rightnode = nilNode
    return nilNode


def removeTempNode():
    '''
    Remove (unlink) the possibly created node using createTempNode()
    nilNode object is global.
    '''
    if nilNode.parent:
        if nilNode is nilNode.parent.leftnode:
            nilNode.parent.leftnode = None
        else:
            nilNode.parent.rightnode = None
