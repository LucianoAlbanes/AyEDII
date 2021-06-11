def hashLinear(key, dictionary,  lengthDictionary):
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
    indexOfKey = key % lengthDictionary # i=0
    increment = 0

    # Search until a empty slot or a key coincidence.
    while dictionary[indexOfKey]:
        if increment == lengthDictionary:
            # Case fullfilled dictionary
            indexOfKey = None
            break
        elif dictionary[indexOfKey] == key:
            break
        else:
            increment += 1
            indexOfKey = (key + increment) % lengthDictionary
    
    # Return the corresponding index.
    return indexOfKey