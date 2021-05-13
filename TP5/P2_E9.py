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


def insert(dictionary, key, value):
    '''
    Explanation:
        Inserts a value in a dictionary (using hash tables).
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

    # Create and add the new node to the list
    add(dictionary[index], key, value)

    # Return the dictionary.
    return dictionary


def delete(dictionary, key):
    '''
    Explanation:
        Deletes a value with the given key from a dictionary.
    Params:
        dictionary: The dictionary on which you want to perform the deletion.
        key: The key of the value to be deleted.
    Return:
        The value of the deleted key.
        If the key do not exists in the dictionary, 'None' will be returned.
    '''
    # Obtain the hash of the given key
    index = h(key)

    # Define a variable to store the value of the possible deleted value.
    deletedValue = None

    # If the index have a LList, search for key coincidences.
    if dictionary[index]:
        if dictionary[index].head.key is key:  # Case head is node to delete
            deletedValue = dictionary[index].head.value  # Store the key
            if not dictionary[index].head.nextNode:  # Unique node, unlink LList
                dictionary[index] = None
            else:  # Have other nodes
                dictionary[index].head = dictionary[index].head.nextNode

        else:  # Key isn't head
            actualNode = dictionary[index].head
            while actualNode.nextNode:  # Loop until key coincidence
                if actualNode.nextNode.key is key:
                    deletedValue = actualNode.nextNode.value  # Store the key
                    actualNode.nextNode = actualNode.nextNode.nextNode
                    break
                actualNode = actualNode.nextNode

    # Return the key if a node was deleted, otherwise None
    return deletedValue


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
    # Define result variable
    isSubset = False

    # set2 must be larger or equal to set1
    if len(set1) > len(set2):
        isSubset = False

    else:  # Possible subset, compare using hash tables.
        # Now, isSubset is true until proven otherwise.
        isSubset = True

        # Define a dictionary to store all the elements of set2
        dictionary = algo1.Array(m, LL.LinkedList())
        for i in range(len(set2)):
            insert(dictionary, set2[i], set2[i])

        # Check existence and delete of each character of set1 in the created dictionary
        for i in range(len(set1)):
            if not delete(dictionary, set1[i]):
                isSubset = False
                break  # When a discrepancy appears, break the loop.

    # Return result
    return isSubset
