# Generic tree data structure
# This tree has a treeNode as a root.
# The children attribute corresponds to an a linked list, where each value attribute is a treeNode.

# Import modules and define classes

from . import linkedlist as LL

class Tree:
    root = None

class TreeNode:
    parent = None
    children = None
    key = None

# Define functions

def createNode(key, parent):
    # Creates and return a new Tree Node, with given parameters.
    newNode = TreeNode()
    newNode.key = key
    newNode.parent = parent
    newNode.children = LL.LinkedList()

    # Add this new node as children of his parent
    if parent:
        LL.add(parent.children, newNode)

    # Return the pointer of the created node
    return newNode
