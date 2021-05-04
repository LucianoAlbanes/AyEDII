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
    Descripción: insert un elemento en T, siendo T un Trie.
    Entrada: El Trie sobre la cual se quiere agregar el elemento (Trie) y
    el valor del elemento (palabra) a agregar.
    Salida: No hay salida definida
    '''
    # Case not initialized tree
    if not trie.root:
        # Initialize trie
        trie.root = TrieNode()
        trie.root.children = LL.LinkedList()

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
    Descripción: Verifica que un elemento se encuentre dentro del Trie
    Entrada: El Trie sobre la cual se quiere buscar el elemento (Trie) y
    el valor del elemento (palabra)
    Salida: Devuelve False o True según se encuentre el elemento.
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
    Descripción: Elimina un elemento se encuentre dentro del Trie
    Entrada: El Trie sobre la cual se quiere eliminar el elemento (Trie)
    y el valor del elemento (palabra) a eliminar.
    Salida: Devuelve False o True según se haya eliminado el elemento.
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
                if currentLevel.isEndOfWord:  # Case 4
                    currentLevel.children = LL.LinkedList()
                    break
        # Return successfully deletion
        return True

    else:  # Is not end of word
        return False
