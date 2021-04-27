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
        RBNode: The RBNode to check if violations exists..
    '''
    while RBNode.parent and RBNode.parent.parent and RBNode.parent.red: #Nontype no tiene red. Es decir que el padre de la raiz no existe, fijate que haces acá jajaj
        if RBNode.parent is RBNode.parent.parent.leftnode:
            uncle = RBNode.parent.parent.rightnode
            if uncle and uncle.red:
                RBNode.parent.red = False # Case 1
                uncle.red = False # Case 1
                RBNode.parent.parent.red = True # Case 1
                RBNode = RBNode.parent.parent
            else:
                if RBNode is RBNode.parent.rightnode:
                    RBNode = RBNode.parent # Case 2
                    rotateLeft(RBTree, RBNode) # Case 2
                RBNode.parent.red = False # Case 3
                RBNode.parent.parent.red = True # Case 3
                rotateRight(RBTree, RBNode.parent.parent) # Case 3
        else:
            uncle = RBNode.parent.parent.leftnode
            if uncle and uncle.red:
                RBNode.parent.red = False # Case 1
                uncle.red = False # Case 1
                RBNode.parent.parent.red = True # Case 1
                RBNode = RBNode.parent.parent
            else:
                if RBNode is RBNode.parent.leftnode:
                    RBNode = RBNode.parent # Case 2
                    rotateRight(RBTree, RBNode) # Case 2
                RBNode.parent.red = False # Case 3
                RBNode.parent.parent.red = True # Case 3
                rotateLeft(RBTree, RBNode.parent.parent) # Case 3
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

    # Return key
    return nodeToDelete.key

def deleteKey(RBTree, key):
    '''
    Explanation:
        Delete an node with a given key on an Red-Black Tree, keeps balanced.
    Params:
        RBTree: The tree on which you want to perform the delete.
        key: The key of the node of the tree to be deleted.
    Return:
        The key of the deleted node.
        Returns 'None' if there is no a node with the given key.
    '''
    # Search the node
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

    # Return key
    return nodeToDelete.key

def deleteAux(RBTree, RBNode):
    # Define check, and store original color
    xNode = RBNode.parent
    successorNode = RBNode
    successorWasRed = isRed(successorNode)

    # Deletetion algorithm
    # Case leaf node
    if not (RBNode.leftnode or RBNode.rightnode):
        if RBNode is RBNode.parent.leftnode:
            RBNode.parent.leftnode = None
        else:
            RBNode.parent.rightnode = None

    # Case right branch
    elif not RBNode.leftnode:
        xNode = RBNode.rightnode
        moveNode(RBTree, RBNode.rightnode, RBNode)

    # Case left branch
    elif not RBNode.rightnode:
        xNode = RBNode.leftnode
        moveNode(RBTree, RBNode.leftnode, RBNode)

    # Case both branchs
    else:
        # Minor of the majors
        successorNode = RBNode.rightnode
        while successorNode.leftnode:
            successorNode = successorNode.leftnode
        
        successorWasRed = isRed(successorNode)
        if successorNode.rightnode:
            xNode = successorNode.rightnode
        else:
            xNode = successorNode

        # Reasign pointers
        if successorNode.parent is RBNode:
            if successorNode.rightnode:
                successorNode.rightnode.parent = successorNode
        else:
            moveNode(RBTree, successorNode.rightnode, successorNode)
            successorNode.rightnode = RBNode.rightnode
            if successorNode.rightnode:
                successorNode.rightnode.parent = successorNode
        
        moveNode(RBTree, successorNode, RBNode)
        successorNode.leftnode = RBNode.leftnode
        successorNode.leftnode.parent = successorNode
        successorNode.red = isRed(RBNode)
    
    # If deleted node was black, proceed to fix the tree.
    if not successorWasRed:
        deleteFixup(RBTree, xNode)

def deleteFixup(RBTree, RBNode):
    '''
    '''
    while (RBNode is not RBTree.root) and (not isRed(RBNode)): # Root or black node stops the while.
        if RBNode is RBNode.parent.leftnode: # RBNode is the left child of his parent
            siblingNode = RBNode.parent.rightnode # Her sibling is the right child of his parent

            if isRed(siblingNode): # Case 1
                siblingNode.red = False
                RBNode.parent.red = True
                rotateLeft(RBTree, RBNode.parent)
                siblingNode = RBNode.parent.rightnode
            
            if siblingNode and not (isRed(siblingNode.leftnode) or isRed(siblingNode.rightnode)): # Case 2
                siblingNode.red = True
                RBNode = RBNode.parent
            
            else: # Case 3 and 4
                if siblingNode and not isRed(siblingNode.rightnode): # Case 3
                    siblingNode.leftnode.red = False
                    siblingNode.red = True
                    rotateRight(RBTree, siblingNode)
                    siblingNode = RBNode.parent.rightnode
                # Case 4
                if siblingNode:
                    siblingNode.red = isRed(RBNode.parent)
                    siblingNode.rightnode.red = False
                RBNode.parent.red = False
                rotateLeft(RBTree, RBNode.parent)
                RBNode = RBTree.root
        
        else: # RBNode is the right child of his parent
            siblingNode = RBNode.parent.leftnode # Her sibling is the right child of his parent

            if isRed(siblingNode): # Case 1
                siblingNode.red = False
                RBNode.parent.red = True
                rotateRight(RBTree, RBNode.parent)
                siblingNode = RBNode.parent.leftnode
            
            if siblingNode and not (isRed(siblingNode.leftnode) or isRed(siblingNode.rightnode)): # Case 2
                siblingNode.red = True
                RBNode = RBNode.parent
            
            else: # Case 3 and 4
                if siblingNode and not isRed(siblingNode.leftnode): # Case 3
                    siblingNode.rightnode.red = False
                    siblingNode.red = True
                    rotateLeft(RBTree, siblingNode)
                    siblingNode = RBNode.parent.leftnode
                # Case 4
                if siblingNode:
                    siblingNode.red = isRed(RBNode.parent)
                    siblingNode.leftnode.red = False
                RBNode.parent.red = False
                rotateRight(RBTree, RBNode.parent)
                RBNode = RBTree.root
    RBNode.red = False

def isRed(RBNode):
    if RBNode:
        return RBNode.red
    else:
        return False # non-existant node = Black

####TESTTTT
# function to print a tree
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
    print(actualNode.red)

    # Process left child.
    printTree(actualNode.leftnode, space)


'''
nums1 = [5,3,4,10,2,9,12,1]
tree = RedBlackTree()
for element in nums1:
    insert(tree, element, element)
delete(tree, 4)
printTree(tree.root,0)
'''



# TEST CODE
import random

miniTree = RedBlackTree()
print('Generando un arbol pequeño, 15 elementos ordenados')
for i in range(1, 19):
    insert(miniTree, i, i)

for i in range(1, 19):
    delete(miniTree, random.randint(0,i))

printTree(miniTree.root, 0)






'''


arreglo = [-819, -725, -825, -657, 908, 94, 788, 142, -315, -899, -255, -76, 785, 87, -853, 64, 39, 214, 432, -915, 541, -703, -319, 839, -832, 655, 227, -89, 610, -277, 109, -826, 848, -580, -188, 698, -405, 195, -627, 310, -349, -39, 358, -699, 595, -834, -763, 211, -866, 620, -704, -926, -169, 862, -631, 383, 737, 947, 151, -370, 108, 401, 540, -289, -623, 260, 662, -454, 625, -887, -985, -205, 720, 30, -346, -455, 631, 948, -719, -103, 145, 930, -282, 635, -525, -811, 181, 566, -667, 110, -986, 328, 909, 106, 71, 929, 773, 994, -956, -907, 510, 530, -40, -165, -467, 695, 52, 865, -779, -567, 175, 940, 76, -988, -637, -931, 117, 145, 351, -51, -452, -667, -295, -243, -429, -842, -666, -368, 186, 856, 45, 562, 940, 808, 731, -114, -830, 246, 153, -382, 284, -178, -745, 981, -873, -256, -301, -929, -10, -57, -102, -536, -83, 258, 429, -652, 622, 409, 292, -55, -362, 883, 133, -9, -497, -273, 541, 123, -650, 210, -188, -868, 447, 533, -549, 796, -522, 947, 487, -194, -718, 946, 288, -875, -711, 247, -567, -98, 734, 573, 719, -827, -743, -684, 711, -746, 816, 836, 980, -51, 446, -585, -358, 964, -570, 875, -585, -426, -299, 949, 603, 327, -849, -885, -293, 241, 874, 334, 774, 157, -9, 490, -113, 415, 443, -585, -199, 326, -549, 219, -843, 132, 305, -480, 444, -1000, 470, 485, -715, 562, -221, -946, 570, -131, 266, -546, -881, 767, 968, 962, 546, 872, 749, -653, -142, 279, -362, 918, 267, -467, -692, -719, 550, 49, -575, -19, -136, 246, -80, -850, 138, 46, 48, -655, -692, -136, -252, -954, 43, 303, 172, -5, 880, -129, -541, 427, -83, 919, 387, 739, 291, -128, 971, 149, -318, 316, 884, -89, -963, 517, 86, 900, 313, -910, -542, -344, 698, -36, -9, -318, 412, -75, -109, -260, -303, -44, -441, 335, 401, 243, -434, -101, 471, -703, 816, 196, -981, -88, -405, -309, -638, 925, -203, 324, 195, 346, -499, 691, 860, 728, 902, 544, -743, -610, 161, -577, -120, 373, 319, 46, -999, 214, -946, -244, -578, 482, 550, 435, 484, -788, 833, -847, -343, 950, -447, -252, 392, 346, 917, 717, -969, 742, -574, 874, -572, -495, 900, -979, 219, -195, 906, -710, -891, 597, 524, -394, 559, 597, 237, 127, -518, -965, -891, 989, -780, -115, -459, 784, 980, -361, -667, 707, -789, 412, 548, -868, 551, 552, 907, -460, -328, -180, -309, 299, 610, -275, -615, -80, 699, -825, 422, 853, -221, 843, 490, 589, 540, -807, -666, 318, -935, 944, 52, 547, -310, 304, 98, 359, 547, -747, 511, -477, -279, -435, 335, -324, -405, -151, -737, -863, 635, 144, -204, -381, 279, -817, 43, -720, 408, 199, 166, 488, 611, -233, -580, 135, -204, 457, -542, -495, -68, 203, -654, -962, -63, -917, 718, -519, -776, -963, 389, 57, 829, 199, -799, 817, 900, -769, -734, 155, -872, -944, -206, 155, -789, -296, 1000, 109, -509, -127]

MrTree = RedBlackTree()

for element in arreglo:
    insert(MrTree, element, element)


countR = 0
countN = 0

def cBF(node):
    global countR
    global countN

    if not node:
        return None

    if node.red:
        countR += 1
    else:
        countN += 1

    cBF(node.leftnode)
    cBF(node.rightnode)

cBF(MrTree.root)
print(f'CountNegra: {countN}')
print(f'CountRojaa: {countR}')
'''