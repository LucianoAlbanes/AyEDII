from lib import algo1, linkedlist as LL

# Def dictionaryNode (analog to linkedlist's node)

class dictionaryNode:
    key = None
    value = None
    nextNode = None


# Define global constant
A = ((5**.5 - 1)/2)  # Golden ratio φ

# Define functions
def h(key):
    '''
    Explanation:
        Generates a hash for a given integer.
    Info:
        This hash function uses 'The multiplication method'
        where (m) is the length of the dictionary and A is φ.
    Params:
        key: The integer from which the hash is to be obtained.
    '''
    return int(m*(key*A % 1))


def insertSet(dictionary, key, value):
    '''
    Explanation:
        Inserts a value in a set dictionary (using hash tables).
    Info:
        Because the dictionary is a set, if the element already exists, won't be added.
    Params:
        dictionary: The dictionary on which you want to perform the insert.
        key: The key of the value to be inserted.
        value: The value to insert in the given dictionary.
    Return:
        The dictionary.
    '''
    # Obtain the hash of the given key
    index = h(key)

    # Create the LinkedList if the index is empty
    if not dictionary[index]:
        dictionary[index] = LL.LinkedList()
    
    if not LL.search(dictionary[index], value):
        # If the value is not in the Llist, add it.
        add(dictionary[index], key, value)
   
    # Return the dictionary.
    return dictionary

def add(linkedList, key, value):
    '''
    Explanation: 
        Add an element at the beginning of a Linked List (sequence ADT).
    Info:
        This add function differs from the implementation of Linked list
        because this function creates a dictionaryNode (which has as an addition a key value).
    Params:
        linkedList: The list on which you want to add the element.
        key: The key of the inserted node.
        value: The value to add.
    '''
    # Create the new node and store value and key.
    newNode = dictionaryNode()
    newNode.key = key
    newNode.value = value

    # Assign the head node to be the second node
    newNode.nextNode = linkedList.head

    # Assign the new node as the first node
    linkedList.head = newNode

def search(dictionary, key):
    '''
    Explanation:
        Searches for a value in the given dictionary and key.
    Params:
        dictionary: The dictionary on which you want to perform the search.
        key: The key of the value to be searched.
    Return:
        The value of element with the given key.
        If the key do not exists in the dictionary, 'None' will be returned.
    '''
    # Obtain the hash of the given key
    index = h(key)

    # Check if the index have a linked list to check if the key exists.
    resultKey = None
    if dictionary[index]:
        actualNode = dictionary[index].head
        while actualNode:
            if actualNode.key is key:
                resultKey = actualNode.value  # Match case
                break
            actualNode = actualNode.nextNode

    # Return the resultKey
    return resultKey


# Exercise specific implementation

def verifySubset(set1, set2):
    '''
    Explanation: 
        Verify if set1 is a subset of set2.
    Params:
        set1: The subset
        set2: The superset
    Return:
        'True' is set1 is a subset of set2.
        'False' otherwise.
    '''
    # Define isSubset. Is true until proven that not.
    isSubset = True

    # Define a dictionary to store all the elements of set2
    dictionary = algo1.Array(m, LL.LinkedList())
    for i in range(len(set2)):
        insertSet(dictionary, set2[i], set2[i]) # Once each

    # Check existence of each character of set1 in the created dictionary
    for i in range(len(set1)):
        if search(dictionary, set1[i]) is None:
            # if that element doesn't exist in the dictionary, set1 isn't a subset
            isSubset = False
            break

    # Return result
    return isSubset

m = 10**digits # 10^(average input digits). Could be smaller.