from mybinarytree import getNode, insertAux
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

# Define fn

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
    if not avlTree.root: # Case if empty tree.
        avlTree.root = newNode
    else: # General case
        insertAux(avlTree.root, newNode)
    
    # Update heights from the inserted node to the root
    calculateHeight(newNode)

    # Update tree's bf
    calculateBalance(avlTree)

    # Rebalance it
    reBalance(avlTree)

    # Return key of inserted node
    return key

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
    calculateHeight(newRoot.leftnode)

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
    calculateHeight(newRoot.rightnode)

    # Return new root pointer
    return newRoot

def calculateBalance(avlTree):
    '''
    Explanation:
        Calculates and sets the balanceFactor parameter of each node of an AVL-Tree.
    Params:
        avlTree: The AVL-Tree in which you want to update their nodes'es balanceFactor.
    Info:
        This function DOESN'T UPDATE HEIGHTS, must be called calculateHeight() first.
    Return:
        The AVL-Tree.
        Returns 'None' if the tree is empty.
    '''
    # Check empty tree
    if not avlTree.root:
        return None
    
    # Call the recursive fn to calculate each bf from root.
    calculateBalanceAux(avlTree.root)

    # Return the tree
    return avlTree

def calculateBalanceAux(avlNode):
    ## This recursive fn calcs and update the bf of avlNode, reading child's heights.
    # Store the height of each child nodes, if exists
    hightL = 0
    hightR = 0
    if avlNode.leftnode:
        hightL = avlNode.leftnode.height + 1
        #Additionally, because this child exists, calculate his bf
        calculateBalanceAux(avlNode.leftnode)

    if avlNode.rightnode:
        hightR = avlNode.rightnode.height + 1
        #Additionally, because this child exists, calculate his bf
        calculateBalanceAux(avlNode.rightnode)

    # Update the bf of the given node
    avlNode.balanceFactor = hightL - hightR

def calculateHeight(avlNode):
    '''
    Explanation:
        Calculates and sets the height parameter from avlNode to the root of an AVL-Tree.
    Params:
        avlNode: The node to update its height, and its parents recursively.
    Return:
        The AVL-Tree.
        Returns 'None' if the tree is empty.
    '''
    ## Re-Calculate height from leaf inserted node to root
    # Case both child nodes
    if avlNode.leftnode and avlNode.rightnode:
        if avlNode.leftnode.height > avlNode.rightnode.height:
            avlNode.height = 1 + avlNode.leftnode.height
        else:
            avlNode.height = 1 + avlNode.rightnode.height
    elif avlNode.leftnode: #Only left child node
        avlNode.height = 1 + avlNode.leftnode.height
    elif avlNode.rightnode: # Only right child node
        avlNode.height = 1 + avlNode.rightnode.height
    else: # Leaf node
        avlNode.height = 0
    
    # Continue up if the avlNode isn't the tree's root
    if avlNode.parent:
        calculateHeight(avlNode.parent)

def reBalance(avlTree):
    '''
    Explanation:
        Checks if the AVL tree is unbalanced and balance it.
    Params:
        avlTree: The AVL-Tree to be balanced.
    Info:
        This function DOESN'T UPDATE BALANCE FACTORS, must be called calculateBalance() first.
    Return:
        The balanced AVL-Tree.
        Returns 'None' if the tree is empty.
    '''
    # Check case empty tree
    if not avlTree.root:
        return None
    
    # Call the recursive fn with root as parameter
    reBalanceAux(avlTree, avlTree.root)

    # Return the balanced tree
    return avlTree

def reBalanceAux(avlTree, avlNode):
    # Case inexistent node
    if not avlNode:
        return None 
    
    # Check if is necessary to rebalance the node (bf != -1,0,1)
    if avlNode.balanceFactor < -1: # unbalanced to the right
        if avlNode.rightnode.balanceFactor > 0: # the rChild have rSubChild
            rotateRight(avlTree, avlNode.rightnode)
            rotateLeft(avlTree, avlNode)
        else: # No rSubrChild
            rotateLeft(avlTree, avlNode)
        
        # Re check actual node
        calculateBalanceAux(avlNode.parent) # Update bf from avlNode
        reBalanceAux(avlTree, avlNode.parent)

    elif avlNode.balanceFactor > 1: # unbalanced to the left
        if avlNode.leftnode.balanceFactor < 0: # same reason
            rotateLeft(avlTree, avlNode.leftnode)
            rotateRight(avlTree, avlNode)
        else:
            rotateRight(avlTree, avlNode)
        
        # Re check actual node
        calculateBalanceAux(avlNode.parent) # Update bf from avlNode
        reBalanceAux(avlTree, avlNode.parent)
    else:
        # Continue recursively.
        reBalanceAux(avlTree, avlNode.leftnode)
        reBalanceAux(avlTree, avlNode.rightnode)
    

#TEST

COUNT = [10]
def printTree(actualNode, space):
    # Base case.
    if not actualNode:
        return None

    # Increase distance between levels.
    space += COUNT[0]

    # Process right child first.
    printTree(actualNode.rightnode, space)

    # Print current node after space.
    print()
    for _ in range(COUNT[0], space):
        print(end=" ")
    print(actualNode.value)

    # Process left child.
    printTree(actualNode.leftnode, space)

tree = AVLTree()

for i in range(0,6):
    i+=1
    insert(tree, i, i)

printTree(tree.root, 0)
print(tree.root.height)