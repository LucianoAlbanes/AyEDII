# Some testing for binary tree adt implementation
import random  # Only for testing
import mybinarytree
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
tree = mybinarytree.BinaryTree()
def x(n):
    mybinarytree.insert(tree, n, n)

#Inserts
nums = [10,8,12,14]
mybinarytree.insert(tree, 'Nico', 15)
mybinarytree.insert(tree, 'Luciano', 19)
mybinarytree.insert(tree, 'Mati', 10)
mybinarytree.insert(tree, 'Humberto', 47)


print(mybinarytree.update(tree, 'Andrea', 47))
print(mybinarytree.getNode(tree, 119))


printTree(tree.root, 0)
