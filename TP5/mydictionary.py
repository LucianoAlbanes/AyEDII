import algo1
import linkedlist as LL

# Def dictionaryNode (analog to linkedlist's node)
class dictionaryNode:
    key = None
    value = None
    nextNode = None


# Define global variables and dictionaries
m = 10 # Length of the dictionary
A = (1 - 5 ** .5) / 2 # Golden ratio φ
dictionary = algo1.Array(m,LL.LinkedList())

# Define functions

def h(key):
    ''' Multiplication method | First, multiply the key by A (φ) and extract the fractional part of kA.
    Then, multiply this value by m and take the floor of the result. '''
    return int(m*(key*A % 1))

def insert(D, key, value):
    '''
    Descripción: Inserta un key en una posición determinada por la función
    de hash similar a (1) en el diccionario (dictionary). Resolver
    colisiones por encadenamiento. En caso de keys duplicados se anexan a
    la lista.
    Entrada: el diccionario sobre el cual se quiere realizar la inserción
    y el valor del key a insertar
    Salida: Devuelve D
    '''
    # Obtain the hash of the given key
    index = h(key)

    # Create the LinkedList if the index is empty
    if not D[index]:
        D[index] = LL.LinkedList()
    
    # Create and add the new node to the list
    add(D[index], key, value)

    # Return the dictionary.
    return D

def search(D, key):
    '''
    Descripción: Busca un key en el diccionario
    Entrada: El diccionario sobre el cual se quiere realizar la búsqueda
    (dictionary) y el valor del key a buscar.
    Salida: Devuelve el value de la key. Devuelve None si el key no se
    encuentra.
    '''
    # Obtain the hash of the given key
    index = h(key)

    # If the index have a LList, search for key coincidences.
    if D[index]:
        actualNode = D[index].head
        while actualNode:
            if actualNode.key is key:
                return actualNode.value # Match case
            actualNode = actualNode.nextNode
    
    # Case empty index or not found key
    return False


def delete(D, key):
    '''
    Descripción: Elimina un key en la posición determinada por una función
    de hash similar (1) del diccionario (dictionary)
    Poscondición: Se debe marcar como nulo el key a eliminar.
    '''
    # Obtain the hash of the given key
    index = h(key)

    # If the index have a LList, search for key coincidences.
    if D[index]:
        if D[index].head.key is key:  # Case head is node to delete
            if not D[index].head.nextNode: # Unique node, unlink LList
                D[index] = None
            else: # Have other nodes
                D[index].head = D[index].head.nextNode
        else: # Key isn't head
            actualNode = D[index].head
            while actualNode.nextNode:
                if actualNode.nextNode.key is key:
                    actualNode.nextNode = actualNode.nextNode.nextNode
                    break
                actualNode = actualNode.nextNode


def add(linkedList, key, value):
    '''
    Explanation: 
        Add an element at the beginning of a LinkedList (sequence ADT).
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


