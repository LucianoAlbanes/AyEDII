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

    # Unlink nilNode from the tree
    removeTempNode()

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

    # Unlink nilNode from the tree
    nilNode.parent.leftnode = None

    # Return key
    return nodeToDelete.key

def deleteAux(RBTree, z):
    y = z
    yColor = y.red
    x = None

    # Case leaf node
    if not (z.leftnode or z.rightnode):
        if z is z.parent.leftnode:
            if z.red:
                z.parent.leftnode = None
            else:
                z.parent.leftnode = createTempNode(z.parent, True)
                x = z.parent.leftnode
        else:
            if z.red:
                z.parent.rightnode = None
            else:
                z.parent.rightnode = createTempNode(z.parent, False)
                x = z.parent.rightnode


    # Case right branch
    elif not z.leftnode:
        x = z.rightnode
        moveNode(RBTree, z.rightnode, z)

    # Case left branch
    elif not z.rightnode:
        x = z.leftnode
        moveNode(RBTree, z.leftnode, z)

    # Case both branchs
    else:
        # Define successor
        y = z.rightnode
        while y.leftnode:
            y = y.leftnode
        
        yColor = y.red
        x = y.rightnode
        if not x: 
            if y.parent.rightnode is y:
                x = createTempNode(y.parent, False)
            else:
                x = createTempNode(y.parent, True)

        # Reasign pointers
        if y.parent is z:
            if x:
                x.parent = y
        else:
            if y.rightnode:
                moveNode(RBTree, y.rightnode, y)
            y.rightnode = z.rightnode
            if y.rightnode:
                y.rightnode.parent = y
        moveNode(RBTree, y, z)
        y.leftnode = z.leftnode
        y.leftnode.parent = y
        y.red = z.red
    
    if not yColor:
        deleteFixup(RBTree, x)

def deleteFixup(RBTree, RBNode):
    while RBNode.parent and not RBNode.red:
        if RBNode is RBNode.parent.leftnode:
            w = RBNode.parent.rightnode
            if isRed(w): # Case 1
                w.red = False
                RBNode.parent.red = True
                rotateLeft(RBTree, RBNode.parent)
                w = RBNode.parent.rightnode

            if not (isRed(w.leftnode) or isRed(w.rightnode)):
                w.red = True
                RBNode = RBNode.parent
            else:
                if not isRed(w.rightnode): # Case 3
                    w.leftnode.red = False
                    w.red = True
                    rotateRight(RBTree, w)
                    w = RBNode.parent.rightnode
                w.red = RBNode.parent.red # Case 4
                RBNode.parent.red = False
                w.rightnode.red = False
                rotateLeft(RBTree, RBNode.parent)
                RBNode = RBTree.root
        else:
            w = RBNode.parent.leftnode
            if w.red: # Case 1
                w.red = False
                RBNode.parent.red = True
                rotateRight(RBTree, RBNode.parent)
                w = RBNode.parent.leftnode

            if not (isRed(w.leftnode) or isRed(w.rightnode)): # Case 2
                w.red = True
                RBNode = RBNode.parent
            else:
                if not isRed(w.leftnode): # Case 3
                    w.rightnode.red = False
                    w.red = True
                    rotateLeft(RBTree, w)
                    w = RBNode.parent.leftnode 
                w.red = RBNode.parent.red # Case 4
                RBNode.parent.red = False
                w.leftnode.red = False
                rotateRight(RBTree, RBNode.parent)
                RBNode = RBTree.root
    RBNode.red = False

def isRed(RBNode):
    if RBNode:
        return RBNode.red
    else:
        return False # non-existant node = Black

def createTempNode(parent, isLeftChild):
    global nilNode
    nilNode.parent = parent
    nilNode.red = False
    if isLeftChild:
        parent.leftnode = nilNode
    else:
        parent.rightnode = nilNode
    return nilNode

def removeTempNode():
    global nilNode
    if nilNode.parent:
        if nilNode is nilNode.parent.leftnode:
            nilNode.parent.leftnode = None
        else:
            nilNode.parent.rightnode = None



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


nums1 = [1,2,3,4,5,6,7,8]
tree = RedBlackTree()
for element in nums1:
    insert(tree, element, element)
delete(tree,2)
printTree(tree.root,0)


# TEST CODE
import random

miniTree = RedBlackTree()
print('Generando un arbol pequeño, 15 elementos ordenados')
for i in range(1, 5000):
    insert(miniTree, random.randint(0,i),random.randint(0,i))

count = 0
for i in range(0, 5000):
    if delete(miniTree, random.randint(0,5000)):
        count +=1

print('----------')
print(count)

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