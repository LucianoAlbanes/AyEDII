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
    
    # Update heights and bfs from the inserted node to the root
    calculateHeight(newNode)
    calculateBalance(newNode, True)

    # Rebalance it
    reBalanceAux(avlTree, newNode)

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

def calculateBalance(avlNode, recursive):
    '''
    Explanation:
        Calculates and sets the balanceFactor parameter from avlNode to the root of an AVL-Tree.
    Params:
        avlNode: The node to update its balanceFactor, and its parents recursively.
    Info:
        This function DOESN'T UPDATE HEIGHTS, must be called calculateHeight() first.
    '''
    ## This recursive fn calcs and update the bf of avlNode, reading child's heights.
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
        calculateBalance(avlNode.parent, True)

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

def reBalanceAux(avlTree, avlNode):
    '''
    Explanation:
        Checks and rebalance an AVL-Tree from avlNode to root.
    Params:
        avlTree: The AVL-Tree to be balanced.
        avlNode: The first node to be checked and rebalanced if is needed.
    Info:
        This function DOESN'T UPDATE BALANCE FACTORS, must be called calculateBalance() first.
    '''
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
        
        # Update balanceFactor of parent's right node ONLY, and from avlNode recursively to top.
        if avlNode.parent.rightnode: calculateBalance(avlNode.parent.rightnode, False) # Update bf from avlNode
        calculateBalance(avlNode, True) # Update bf from avlNode

    elif avlNode.balanceFactor > 1: # unbalanced to the left
        if avlNode.leftnode.balanceFactor < 0: # same reason
            rotateLeft(avlTree, avlNode.leftnode)
            rotateRight(avlTree, avlNode)
        else:
            rotateRight(avlTree, avlNode)
        
        # Update balanceFactor of parent's left node ONLY, and from avlNode recursively to top.
        if avlNode.parent.leftnode: calculateBalance(avlNode.parent.leftnode, False) # Update bf from avlNode
        calculateBalance(avlNode, True) # Update bf from avlNode
    else:
        # Continue recursively until root
        reBalanceAux(avlTree, avlNode.parent)
    

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
import random
for i in range(1,5000):
    f =random.randint(-999999,9999999)
    insert(tree, i,i)
    print(i)

### Checks if bf arfe ok
def cBF(node):
    if not node:
        return None

    hightL = 0
    hightR = 0
    
    if node.leftnode:
        hightL = node.leftnode.height + 1
    if node.rightnode:
        hightR = node.rightnode.height + 1

    
    if (node.balanceFactor != hightL - hightR):
        print(f'here at: {node.value}')
    else:
        cBF(node.leftnode)
        cBF(node.rightnode)

cBF(tree.root)
print(tree.root.height)
print(tree.root.balanceFactor)