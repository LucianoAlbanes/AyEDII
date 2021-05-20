# Some operations to do with arrays.

# Search for an element on an array.
def search(array, element):
    '''
    Explanation: 
        Searches for an element in the given array.
    Params:
        array: The array on which you want to perform the search.
        element: The element to search in the given array.
    Return:
        The index where is the element.
        If the element is found multiple times, returns the first index where appears.
        Returns 'None' if the element is not in the array.
    '''
    index = None
    for i in range(0, len(array)):
        if array[i] == element:
            index = i
            break
    return index

# Insert an element on an array
def insert(array, element, position):
    '''
    Explanation:
        Inserts an element in a given position on an array.
    Info:
        All other elements are moved one position down.
        The last element will be lost.
    Params:
        array: The array on which you want to perform the insert.
        element: The element to insert in the given array.
        position: The position of the element to insert.
    Return:
        The index where was inserted the element.
        Returns None' if the element can't be inserted.
    '''
    # Store the length of the array.
    length = len(array)

    # Case if the position is out of bounds.
    if position >= length:
        return None

    # Moving the rest of the elements one position.
    for i in range(length-1, position, -1):
        array[i] = array[i-1]

    # Assing the element to the given position.
    array[position] = element

    # Return the element position.
    return position

# Delete an element on an array.
def delete(array, element):
    '''
    Explanation:
        Delete an element on an array.
    Info:
        All other elements are moved one position up.
        The last element will be 'None'.
        If exist more than one element, only the first one will be deleted.
    Params:
        array: The array on which you want to perform the delete.
        element: The element to delete in the given array.
    Return:
        The index where was located the deleted element.
        Returns 'None' if the element don't exist on the array.
    '''
    # Store the length of the array.
    length = len(array)

    # Search for the index of the element.
    index = search(array, element)

    # Check if none, and end. Otherwise do the deletion.
    if index == None:
        return None
    else:
        # Move one position up from the index of the element deleted.
        for i in range(index, length-1):
            array[i] = array[i+1]
        # Assign the last element of the array to 'None'.
        array[length-1] = None
        # Return the index where was located the deleted element.
        return index

# Count the lenght of the array (without empty elements)
def length(array):
    '''
    Explanation: 
        Count the number of active elements in the array.
    Params:
        array: The array on which you want to perform the count.
    Return:
        The number of items that are not 'None'.
    '''
    count = 0
    for i in range(0, len(array)):
        if array[i] != None:
            count += 1
    return count
