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

def cmpStrPermutation(str1, str2):
    '''
    Explanation: 
        Compares if a string is a permutation of another.
    Params:
        str1: The first string.
        str2: The second string.
    Return:
        'True' is str1 is a permutation of str2.
        'False' otherwise.
    '''
    # Define result variable
    isPermutation = False

    # Check if the two str have same length. Otherwise is not a permutation.
    if len(str1) != len(str2):
        isPermutation = False

    else:  # Same length, compare using hash tables.
        # Now, isPermutation is true until proven otherwise.
        isPermutation = True

        # Define a dictionary to store each character of str1
        dictionary = algo1.Array(m, LL.LinkedList())
        for i in range(len(str1)):
            # ord() return unicode code of char
            insert(dictionary, ord(str1[i]), str1[i])

        # Check existence and delete of each character of str2 in the created dictionary
        for i in range(len(str2)):
            if not delete(dictionary, ord(str2[i])):
                isPermutation = False
                break  # When a discrepancy appears, break the loop.

    # Return result
    return isPermutation


# Define length
m = 94  # Length of the dictionary (Basic latin, punctuation and symbols)
