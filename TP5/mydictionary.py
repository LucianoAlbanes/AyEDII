from lib import algo1, linkedlist as LL

# Def dictionaryNode (analog to linkedlist's node)

class dictionaryNode:
    key = None
    value = None
    nextNode = None


# Define global constants and dictionaries
m = 10  # Length of the dictionary
dictionary = algo1.Array(m, LL.LinkedList())

# Define functions

def h(key):
    '''
    Explanation:
        Generates a hash for a given integer.
    Info:
        This hash function uses 'The division method' (key % m)
        where (m) is the length of the dictionary.
    Params:
        key: The integer from which the hash is to be obtained.
    '''
    return (key % m)


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
