# Some testing for binary tree adt implementation
import random  # Only for testing
from mybinarytree import BinaryTree, insert, deleteKey, traverseInPreOrder
from linkedlist import access, length


def printList(linkedList):
    print('[', end="")
    for i in range(0, length(linkedList)):
        if i != 0:
            print(', ', end="")
        print(str((access(linkedList, i)).key), end="")
    print(']')


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
    print(actualNode.key)

    # Process left child.
    printTree(actualNode.leftnode, space)


# TEST CODE

# Create a tree
tree = BinaryTree()
def x(n):
    insert(tree, n, n)

#Inserts
nums = [10,8,12,14]
for n in nums:
    x(n)


#print
deleteKey(tree,12)
printTree(tree.root,0)

'''
print('\n-------------------------\nárbol binario casi aleatorio (?\n-------------------------\n')

printTree(tree.root, 0)

print('\n-------------------------\nEliminando hojas 101 y -1\n-------------------------\n')

delete(tree, 'LeafR')
delete(tree, 'LeafL')
printTree(tree.root, 0)

print('\n-------------------------\nImprimiendo keys en pre orden\n-------------------------\n')

'''
printList(traverseInPreOrder(tree))
