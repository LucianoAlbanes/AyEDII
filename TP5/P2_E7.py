from lib import algo1, linkedlist as LL

# Def dictionaryNode (analog to linkedlist's node)


class dictionaryNode:
    key = None
    value = None
    nextNode = None

# Define functions


def h(key):
    '''
    Explanation:
        Get the position in the alphabet for a given character.
    Info:
        This function is specific to letters from a-z and A-Z. (ϵ ñ,Ñ).
        The dictionary length is 54 (27*2)
    Params:
        key: The letter from which the hash is to be obtained.
    Return:
        An integer with the hash (position) of the given letter in the alphabet.
    '''
    # Define dictionary length and result variable
    result = None

    # Store unicode value of key
    if key == 'Ñ':
        result = 14
    elif key == 'ñ':
        result = 41
    else:
        # Define result using 26 letter alphabet
        result = ord(key) - ord('A')

        # Fix to consider ñ in alphabet and other unicode characters
        if result >= 14 and result <= 26:
            result += 1
        elif result > 26 and result <= 45:
            result -= 5
        elif result > 40:
            result -= 4

    # Return the position of the key in a 27 letter alphabet
    return result


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


def zipString(string):
    '''
    Explanation:
        Compress a given string like the following pattern: 'aabcccccaaa' -> 'a2b1c5a3'.
    Info:
        If the result string is grater or equal to the given string, this last one will be returned.
    Params:
        string: The string to be compresed.
    Return:
        The compressed string or the input, as explained in 'Info'.
    '''
    # Define length of dictionary and create one
    m = 27*2  # Two alphabets, upper and lower case
    dictionary = algo1.Array(m, LL.LinkedList())

    # Load values of the string in the dictionary:
    # key: hash of the letter, value: times that appears.
    # Will be added in inverse order, to mantain order and
    # get better time performance when accessing at the linked list.
    i = len(string)-1
    while i >= 0:
        actualLetter = string[i]
        timesAppear = 1
        while i > 0 and actualLetter == string[i-1]:
            timesAppear += 1
            i -= 1
        insert(dictionary, actualLetter, timesAppear)
        i -= 1

    # Define a output string to store contatenating each letter with his
    # respective value on the dictionary 'timesAppears', using delete().
    outputString = ''
    for i in range(0, len(string)):
        if i == len(string)-1 or string[i] != string[i+1]:
            outputString = (
                outputString + string[i] + str(delete(dictionary, string[i])))

    # If original input is shorter or equal to the result,
    # overwrite the output string with the original one.
    if len(string) <= len(outputString):
        outputString = string

    # Return the final output string
    return outputString
