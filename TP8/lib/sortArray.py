from .algo1 import *

# Insertion sort

def insertionSortR(array):
    '''
    Returns a new array sorted in reverse order.
    '''
    # Define a new array and copy elements
    outputArray = Array(len(array), 0)
    for i in range(len(array)):
        outputArray[i] = array[i]

    # Sort in reverse order
    for i in range(1, len(outputArray)):
        temp = outputArray[i]
        j = i - 1

        while j >= 0 and temp > outputArray[j]:
            outputArray[j+1] = outputArray[j]
            outputArray[j] = temp
            j -= 1

    # Return sorted array
    return outputArray
