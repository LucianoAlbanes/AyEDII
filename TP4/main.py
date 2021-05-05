import linkedlist as LL
import algo1 as algo


def searchPattern(trie, word, length):
    '''
    Explanation:
        Searchs for words with a given prefix with the given length.
    Params:
        trie: The trie on which you want to perform the operation.
        word: The prefix of the words to be searched.
        length: The length of the searched words.
    Return:
        A linked list with the words (as arrays) that satisfy the conditions.
        Additionally, prints these words.
        'False' if the given parameters are not valid.
    '''
    # Convert input element into a array
    text = algo.String(word)

    # Check length of word <= length
    if len(text) > length:
        return False

    # Comprare each level with each index of 'text'
    currentLevel = trie.root

    for i in range(0, len(text)):
        found = False  # Flag existant key
        currentNode = currentLevel.children.head

        # Search for index in current level
        while currentNode and not found:
            if currentNode.value.key is text[i]:
                found = True
            else:
                currentNode = currentNode.nextNode

        # Return here if not exist current index
        if not found:
            return False
        else:
            currentLevel = currentNode.value

    # Create a linked list to store the results
    listOfWords = LL.LinkedList()

    # Navigate each child node recursively, use aux fn to check and store words.
    searchPatternAux(currentNode.value,
                     (length-len(word)), listOfWords, length)

    # Print each matched word
    listNode = listOfWords.head
    while listNode:
        print(listNode.value)
        listNode = listNode.nextNode

    # Return the list of matched words
    return listOfWords


def searchPatternAux(currentLevel, remainingLength, listOfWords, length):
    if remainingLength > 0:  # Continue recursively with each children until length == depth.
        currentNode = currentLevel.children.head
        while currentNode:
            searchPatternAux(currentNode.value,
                             remainingLength-1, listOfWords, length)
            currentNode = currentNode.nextNode
    else:
        if currentLevel.isEndOfWord:  # Match case
            # Add an array in the Linked list
            LL.add(listOfWords, algo.Array(length, ''))
            for i in range(0, length):  # Store each value
                listOfWords.head.value[length-i-1] = currentLevel.key
                currentLevel = currentLevel.parent


def checkEqual(trieA, trieB):
    '''
    Explanation:
        Check if two given tries contain the same words.
    Params:
        trieA: The first trie on which you want to perform the operation.
        trieB: The second trie on which you want to perform the operation.
    Return:
        'True' if both tries contain the same words. Otherwise, 'False'
    '''
    # Store flag result
    result = True

    # Special Cases
    if not (trieA.root or trieB.root):  # Both trees empty
        return True
    elif not (trieA.root and trieB.root):  # One tree empty
        result = False
    # Search recursively
    else:
        result = checkEqualAux(trieA.root, trieB.root)

    # Return
    return result


def checkEqualAux(trieNodeA, trieNodeB):
    result = True  # Define flag

    # Case only one level exist
    if bool(trieNodeA) != bool(trieNodeB):  # XOR
        result = False

    # Check lengths of the two childes
    elif LL.length(trieNodeA.children) != LL.length(trieNodeB.children):
        result = False

    # Check existence of each key on both LLists
    else:
        # Check actual level
        actualNodeA = trieNodeA.children.head
        while result and actualNodeA:
            actualNodeB = getNodeByKey(
                trieNodeB.children, actualNodeA.value.key)
            if actualNodeB is None:  # Check key existence
                result = False
            # XOR .isEndOfWord
            elif bool(actualNodeA.value.isEndOfWord) != bool(actualNodeB.value.isEndOfWord):
                result = False
            actualNodeA = actualNodeA.nextNode

        # Check deeper levels recursively
        actualNodeA = trieNodeA.children.head
        while result and actualNodeA:
            actualNodeB = getNodeByKey(
                trieNodeB.children, actualNodeA.value.key)
            result = (checkEqualAux(actualNodeA.value, actualNodeB.value))
            actualNodeA = actualNodeA.nextNode

    # Return the result
    return result


def getNodeByKey(linkedList, key):
    """
    Explanation: 
        Searches for an key in a given linkedlist of TrieNodes.
    Params:
        linkedList: The list on which you want to perform the operation.
        key: The key to search in the given list.
    Return:
        The index where is the element.
        Returns 'None' if the element is not in the list.
    """
    # Define the head of the linked list as the actualNode
    actualNode = linkedList.head

    # Perform the search
    i = -1  # To start with 0
    while actualNode:
        i += 1
        if actualNode.value.key == key:
            return actualNode
        actualNode = actualNode.nextNode
    return None


def checkInvert(trie):
    '''
    Explanation:
        Checks if in a trie there is a word that is the inverse of another one.
    Params:
        trie: The trie on which you want to perform the operation.
    Return:
        'True' if exist a word that is the inverse of another. Otherwise, 'False'
    '''
    # Generate a LList to store words
    listOfWords = LL.LinkedList()

    # Check all the nodes recursively
    result = checkInvertAux(trie.root, listOfWords, False)

    # Return the result
    return result


def checkInvertAux(trieNode, listOfWords, foundFlag):
    # Empty trie node case or already found pair of word
    if foundFlag or not trieNode:
        return False

    # Match case
    if trieNode.isEndOfWord:
        # Store the word in a temp linked list
        thisWord = LL.LinkedList()
        actualNode = trieNode
        while actualNode.parent:
            LL.add(thisWord, actualNode.key)
            actualNode = actualNode.parent

        # Store the word as an array in the listOfWords
        lengthOfThisWord = LL.length(thisWord)
        LL.add(listOfWords, algo.Array(lengthOfThisWord, ''))
        actualNode = thisWord.head
        for i in range(0, lengthOfThisWord):
            listOfWords.head.value[i] = actualNode.value
            actualNode = actualNode.nextNode

        # Check if this word is the inverse of any of the previously saved words in 'listOfWords'
        foundFlag = searchInverse(listOfWords)

    # Call recursively
    actualNode = trieNode.children.head
    while not foundFlag and actualNode:
        foundFlag = checkInvertAux(actualNode.value, listOfWords, foundFlag)
        actualNode = actualNode.nextNode

    # Return the foundFlag
    return foundFlag


def searchInverse(listOfWords):
    # Define words
    lastFoundWord = listOfWords.head
    currentWord = listOfWords.head.nextNode
    foundFlag = False
    # Check the reaming words in the linked list.
    while not foundFlag and currentWord:
        if len(lastFoundWord.value) == len(currentWord.value):  # Same length
            invertedFlag = True
            length = len(lastFoundWord.value)
            for i in range(0, length):
                if invertedFlag and lastFoundWord.value[i] != currentWord.value[length-i-1]:
                    invertedFlag = False
            foundFlag = invertedFlag
        currentWord = currentWord.nextNode
    return foundFlag
