# Queue implementation (FIFO) [O(1)]

# Differs from the queue implemented in 'Algoritmos y Estructuras de Datos 1'.
# This implementation of queue uses a modified linked list,
# (simple linked) but with a tail attribute, and each node stores the queued node after it

# Define classes

class Queue:
    head = None
    tail = None

class QueueNode:
    previousNode = None
    value = None

# Define functions

def enqueue(queue, element):
    '''
    Explanation: 
        Add an element at the beginning of a queue.
    Params:
        queue: The queue on which you want to add the element.
        element: The element to add.
    Return:
        The pointer of the node of the added element.
    '''

    # Add the element to the beginning of the queue. add() equivalent.
    newNode = QueueNode()
    newNode.value = element

    # Update previousNode in the old head.
    if queue.head:
       queue.head.previousNode = newNode
    else:
        # If there is not elements in the queue, the newNode will be head and tail simuntaniolsy
        queue.tail = newNode

    # Define newNode as the queue's head
    queue.head = newNode

    # Return the pointer of the added node
    return newNode


def dequeue(queue):
    '''
    Explanation: 
        Extract the first element added to the queue.
    Info:
        The extracted element will be removed from the queue.
    Params:
        queue: The queue on which you want perform the extraction.
    Return:
        The extracted element.
        Returns 'None' if the queue is empty.
    '''
    # Define a variable to store the element to be returned
    element = None

    # Checks if exist an a tail in the queue
    if queue.tail:
        # Store the element
        element = queue.tail.value

        # Unlink that node from the queue and
        queue.tail = queue.tail.previousNode

        # Verify case when the queue was emptied, remove head too
        if not queue.tail:
            queue.head = None
    
    # Return the element
    return element
