'''
Implementar un algoritmo que ordene una lista de elementos donde siempre el elemento del
medio de la lista contiene antes que él en la lista la mitad de los elementos menores que él.
Explique la estrategia de ordenación utilizada.
'''
from linkedlist import length, getNode, swapNodes
from quickSort import quickSort
from math import floor

def sort(linkedList):
    if checkConditions(linkedList): # Check if the list is already ordered
        print('OK')
        return linkedList
    else:
        lengthOfList = length(linkedList)
        middleIndex = round((lengthOfList-1)/2)
        
        for i in range(middleIndex+1, lengthOfList):
            swapNodes(linkedList, middleIndex, i)
            if checkConditions(linkedList): break

        if checkConditions(linkedList):
            printList(linkedList)
            print('OK^ORDERED')
        else:
            print('FAIL')
        

def checkConditions(linkedList):
    ##Verify if the given list satisfy the conditions, return a boolean value
    lengthOfList = length(linkedList)
    
    middleIndex = round((lengthOfList-1)/2)
    middleNode = getNode(linkedList, middleIndex)

    minorNumbersAllowed = round(lengthOfList/4) #How much numbers must be less than the middle

    actualNode = linkedList.head
    while actualNode != middleNode:
        if actualNode.value < middleNode.value:
            minorNumbersAllowed -= 1
        if minorNumbersAllowed < 0: break
        actualNode = actualNode.nextNode
    return minorNumbersAllowed == 0


# ~~~ Test code ~~~
from random import randint
from linkedlist import LinkedList, add, access

# Define a fn to print a Linked List
def printList(linkedList):
    print('[', end="")
    for i in range(0, length(linkedList)):
        if i != 0:
            print(', ', end="")
        print(str(access(linkedList, i)), end="")
    print(']')

# Create a linked list and fill it with 10 random integers
listOfNumbers = LinkedList()
for _ in range(0, 7):
    add(listOfNumbers, randint(0, 10))

# Check
printList(listOfNumbers)
sort(listOfNumbers)

