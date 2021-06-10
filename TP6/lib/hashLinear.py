def hashLinear(key, dictionary):
    '''
    Explanation:
        Returns the corresponding index of a given key in a dictionary 
    Info:
        This hash function uses open hashing (linear probing).
    Params:
        key: An integer
        dictionary: The dictionary where you want to access / insert the key.
    '''
    # Define useful constants
    dictionarySize = len(dictionary)
    indexOfKey = key % dictionarySize # i=0
    increment = 0

    # Search until a empty slot or a key coincidence.
    while dictionary[indexOfKey]:
        if increment == dictionarySize:
            # Case fullfilled dictionary
            indexOfKey = None
            break
        
        if dictionary[indexOfKey].key == key:
            break
        else:
            increment += 1
            indexOfKey = (key + increment) % dictionarySize
    
    # Return the corresponding index.
    return indexOfKey