# Trie data structure implementation
import linkedlist as LL
import algo1 as algo
# Define classes


class Trie:
    root = None


class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False

# Define functions


def insert(trie, element):
    '''
    Explanation:
        Inserts an element in a given trie.
    Params:
        trie: The trie on which you want to perform the insert.
        element: The word to insert in the given trie.
    Return:
        Not defined.
    '''
    # Case not initialized tree
    if not trie.root:
        # Initialize trie
        trie.root = TrieNode()
        trie.root.children = LL.LinkedList()

    # Convert input element into an array.
    text = algo.String(element)

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

        if not found:
            # Create the new trie node
            newNode = TrieNode()
            newNode.parent = currentLevel
            newNode.key = text[i]
            newNode.children = LL.LinkedList()
            LL.add(currentLevel.children, newNode)
            currentLevel = newNode
        else:
            currentLevel = currentNode.value

    # Set end of word
    currentLevel.isEndOfWord = True


def search(trie, element):
    '''
    Explanation: 
        Searches for an element in the given trie.
    Params:
        trie: The trie on which you want to perform the search.
        element: The word to search in the given trie.
    Return:
        'True' if the element is in the given trie. Otherwise 'False'.
    '''
    # Convert input element into a array
    text = algo.String(element)

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

    # Check condition isEndOfWord
    if currentLevel.isEndOfWord:
        return True
    else:
        return False


def delete(trie, element):
    '''
    Explanation:
        Delete an element from a trie.
    Params:
        trie: The trie on which you want to perform the delete.
        element: The word to delete in the given trie.
    Return:
        'True' if the deletion was successful.
        'False' if the given element is not in the trie.
    '''
    # Convert input element into a array
    text = algo.String(element)

    # Comprare each level with each index of 'text'
    currentLevel = trie.root

    # Search last node of the word
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
        if not found:  # Case 1
            return False
        else:
            currentLevel = currentNode.value

    # Check condition isEndOfWord
    if currentLevel.isEndOfWord:
        if currentLevel.children.head:  # Case 3 - Prefix of another word
            currentLevel.isEndOfWord = False
        else:
            while (currentLevel.parent.children.head.value is currentLevel and not currentLevel.parent.children.head.nextNode):
                currentLevel.children = LL.LinkedList()
                currentLevel = currentLevel.parent  # Case 2
                if not currentLevel.parent:
                    currentLevel.children = LL.LinkedList()  # Case empty tree (root)
                    break
                if currentLevel.isEndOfWord:  # Case 4
                    currentLevel.children = LL.LinkedList()
                    break
        # Return successfully deletion
        return True

    else:  # The word not exists in the trie, apears but without .isEndOfWord
        return False
