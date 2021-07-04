# Part 3 of 'Análisis y Diseño de Algoritmos'
# Divide and conquer


# Exercise 9


def busquedaKesimo(numberList, index):
    '''
    Explanation:
        Searches the value corresponding to the given index if the array were sorted.
    Parameters:
        numbersList: An array with numbers where to find the value.
        index: The position in the array (if were sorted) of the element to be found.
    Return:
        The value of the found element.
    '''
    # Define variables
    result = None
    length = len(numberList)

    # Verify valid index and search with divide and conquer
    if index < length:
        result = divideBK(numberList, 0, length-1, index)

    # Return the result
    return result


def divideBK(array, low, high, index):
    ''' Recursive part of busquedaKesimo, (partitioning like quicksort)'''
    # Select pivot (Median of three)
    a = array[low]
    b = array[int((low+high)/2)]
    c = array[high]

    if (a <= b <= c) or (c <= b <= a):
        pivot = int((low+high)/2)
    elif (b <= a <= c) or (c <= a <= b):
        pivot = low
    else:
        pivot = high

    # Sort (QuickSort like algorithm)
    # Swap the pivot with the low element
    temp = array[low]
    array[low] = array[pivot]
    array[pivot] = temp

    # Swap the elements with lower value than the pivot
    border = low  # starts at pivot
    for i in range(low, high+1):
        if array[i] < array[low]:
            border += 1
            temp = array[border]
            array[border] = array[i]
            array[i] = temp

    # Verify final pos of the pivot. If match with index, return it. otherwise contine recursion
    result = None
    if border == index:
        # Base case. Get the value and return it
        result = array[low]
    else:
        # General case
        # Return pivot to correct position
        temp = array[low]
        array[low] = array[border]
        array[border] = temp

        # Continue recursion with useful part
        if border < index:
            result = divideBK(array, border+1, high, index)
        else:
            result = divideBK(array, low, border-1, index)

    # Return
    return result


# TEST
a = [99, 33, 88, 66, 22, 55, 11, 77, 44, 00]
for i in range(10):
    print(busquedaKesimo(a, i))
