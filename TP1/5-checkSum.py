def checkIfSumExist(linkedList, n):
    '''
    Explanation:
        Check if the number n exists as a sum of two elements of the given list.
    Params:
        linkedList: A Linked list where the elements are located.
        n: The desired sum
    Return:
        Returns True if there exist two elements in the list such their sum equals to n.
        Otherwise, False.
    '''
    actualNodeA = linkedList.head
    while actualNodeA:
        actualNodeB = actualNodeA.nextNode
        while actualNodeB:
            if (actualNodeA.value + actualNodeB.value == n):
                return True
            actualNodeB = actualNodeB.nextNode
        actualNodeA = actualNodeA.nextNode
    return False


# ~~~ Test code ~~~
from random import randint
from linkedlist import LinkedList, add, access, length

# Define a fn to print a Linked List
def printList(linkedList):
    print('[', end="")
    for i in range(0, length(linkedList)):
        if i != 0:
            print(', ', end="")
        print(str(access(linkedList, i)), end="")
    print(']')

# Create a linked list and fill it with 10 random integers, and a random sum to check
listOfNumbers = LinkedList()
for _ in range(0, 10):
    add(listOfNumbers, randint(0, 10))
nSum = randint(0,20)

# Check main function
printList(listOfNumbers)
print(f'Contiene ({nSum}) como la suma de dos de sus elementos = {checkIfSumExist(listOfNumbers, nSum)}')