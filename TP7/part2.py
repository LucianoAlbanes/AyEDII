# Implementation of patter matching exercises
# Part 2 of Pattern Matching
from lib.algo1 import *
from lib.strcmpAlt import *
from lib.hashLinear import hashLinear as h


# Find biggest prefix

def findBiggestPrefix(string, prefixStr):
    '''
    Explanation: 
        Searchs for the biggest prefix of one string in another.
    Params:
        string: The string where will be searched for the ocurrences of prefixes.
        prefixStr: The string to extract prefixes
    Return:
        An integer with the position where the biggest prefix starts inside the string.
        'None' if there are not prefixes.
    '''
    # Define a result to store how many characters was found as prefix
    charactersFound = 0

    # Store lengths of both strings
    lengthS = len(string)
    lengthP = len(prefixStr)

    # Check requisites for general case
    if not strcmpAlt(prefixStr, String('')):
        # Calc the hash of strings of length 1
        hashS = ord(string[0])
        hashP = ord(prefixStr[0])

        # Save where the biggest prefix was found
        foundAt = 0

        # Explore the string until match
        i = 0
        while i < (lengthS-foundAt):

            # Check if hashes match, compare and increment (new biggest prefix found)
            while hashS == hashP and strcmp(substr(string, i, i+charactersFound), substr(prefixStr, 0, charactersFound)):
                foundAt = i
                charactersFound += 1
                if charactersFound == lengthP or foundAt+charactersFound == lengthS:  # Max prefix reached
                    break
                hashS = 128*hashS + ord(string[i+charactersFound])
                hashP = 128*hashP + ord(prefixStr[charactersFound])

            # Rehash (+1 position)
            if i < lengthS-charactersFound-1:
                hashS -= (ord(string[i])*(128**(charactersFound)))
                hashS = hashS*128
                hashS += ord(string[charactersFound+i+1])

            # Increment while loop
            i += 1

    # Verify return
    result = None
    if charactersFound > 0:
        result = foundAt
    return result


# Rabin Karp

def RK_matcher(string, pattern):
    '''
    Explanation: 
        Searchs if the pattern is contained on string.
    Params:
        string: The string where will be searched the occurrence of pattern.
        pattern: The pattern (string) to be searched.
    Return:
        An integer with the position where the pattern starts inside the string.
        'None' if was not found.
    '''
    # Define a variable to store the return of this function (index where apears)
    result = None

    # Store lengths of both strings
    lengthS = len(string)
    lengthP = len(pattern)

    # Check case same length, no need to search, only compare
    if lengthS == lengthP:
        if strcmp(string, pattern):
            result = 0

    # Check requisites for general case
    elif not (strcmpAlt(pattern, String('')) or lengthP > lengthS):
        # Calc the hash of the pattern and string[0:lengthP]
        hashS = 0
        hashP = 0
        for i in range(lengthP):
            hashS += ord(string[i])*(128**(lengthP-i-1))
            hashP += ord(pattern[i])*(128**(lengthP-i-1))

        # Explore the string until match
        for i in range(lengthS-lengthP+1):
            # Check if hashes match
            if hashS == hashP:
                # Possible coincidence, do strcmp()
                if strcmp(substr(string, i, i+lengthP), pattern):
                    # Here!
                    result = i
                    break

            # Rehash
            if i != lengthS-lengthP:
                hashS -= (ord(string[i])*(128**(lengthP-1)))
                hashS = hashS*128
                hashS += ord(string[lengthP+i])

        # Return the result
        return result


# Finite automata

def FA_matcher(string, statesArray, finalState):
    '''
    Explanation: 
        Searchs if a given state is reachable from the given string.
    Params:
        string: The string where will be searched the occurrence of pattern.
        statesArray: The array that contains the states of the finite automata.
        finalState: The desired state to reach.
    Return:
        An integer with the position where the pattern starts inside the string.
        'None' if was not found.
    '''
    result = None
    currentState = 0
    lengthAlphabet = len(statesArray[0])

    # Explore until match
    for i in range(len(string)):
        # Get index of character from the first row
        charIndex = h(ord(string[i]), statesArray[0], lengthAlphabet)

        if charIndex != None:  # Verify if is part of the alphabet
            currentState = statesArray[currentState+1][charIndex]
            if currentState == finalState:
                result = i-finalState+1
                break
        else:
            # An unrecognized character appears, start again from state 0
            currentState = 0
    return result


def FA_computeTransition(pattern, alphabet):
    '''
    Explanation:
        Generates the arrays of states of the finite automata for the given pattern.
    Params:
        pattern: The string to be analyzed from which the states will be generated 
        alphabet: Each diffrent character included in pattern.
    Return:
        An Array, representing the states table of the finite automata.
    '''
    def minimum(a, b):
        result = a
        if b < a:
            result = a
        return result

    def isSuffix(suffix, word):
        match = True  # Until proven otherwise
        lenS = len(suffix)
        lenW = len(word)

        if lenS <= lenW:
            for i in range(lenS):
                if not strcmp(suffix[i], word[lenW-lenS+i]):
                    match = False
                    break
        else:
            # Overflow, can't be suffix
            match = False
        return match

    # Calc and save length of both strings
    lengthP = len(pattern)
    lengthA = len(alphabet)

    # Define an array of |P|*|𝛴| to store the finite automata function
    # The first row will be used to store the unicode code point of the corresponding character
    FA_Function = Array(lengthP+1, Array(lengthA, 0))

    # Store each character of alphabet in the first row
    for i in range(lengthA):
        unicodeCode = ord(alphabet[i])
        FA_Function[0][h(unicodeCode, FA_Function[0], lengthA)] = unicodeCode

    # Find states (copy paste from CLRS)
    for q in range(0, lengthP):
        for a in range(lengthA):
            k = minimum((lengthP+1), (q+2))
            k -= 1
            while not isSuffix(substr(pattern, 0, k), concat(substr(pattern, 0, q), String(alphabet[a]))):
                k -= 1
            FA_Function[q+1][h(ord(alphabet[a]), FA_Function[0], lengthA)] = k
    return FA_Function

# Knuth Morris Pratt


def KMP_matcher(string, pattern):
    '''
    Explanation: 
        Searchs if the pattern is contained on string.
    Params:
        string: The string where will be searched the occurrence of pattern.
        pattern: The pattern (string) to be searched.
    Return:
        An integer with the position where the pattern starts inside the string.
        'None' if was not found.
    '''
    # Define a variable to store the return of this function (index where apears)
    result = None

    # Store lengths of both strings
    lengthS = len(string)
    lengthP = len(pattern)

    # Check case same length, no need to search, only compare
    if lengthS == lengthP:
        if strcmp(string, pattern):
            result = 0

    # Check requisites for general case
    else:
        prefixFn = KMP_computePrefixFn(pattern)
        matched = 0
        for i in range(lengthS):
            while matched > 0 and not strcmp(pattern[matched], string[i]):
                matched = prefixFn[matched-1]

            if strcmp(pattern[matched], string[i]):
                matched += 1

            if matched == lengthP:
                result = i - (lengthP-1)

    # Return the result
    return result


def KMP_computePrefixFn(pattern):
    '''
    Explanation:
        Generates the prefixes function of the given pattern.
    Params:
        pattern: The string to be analyzed from which the prefix function will be created.
    Return:
        An Array (n*1).
    '''
    lengthP = len(pattern)
    prefixFn = Array(lengthP, 0)
    prefixFn[0] = 0
    k = 0

    for q in range(2, lengthP+1):
        while k > 0 and not strcmp(pattern[k], pattern[q-1]):
            k = prefixFn[k-1]

        if strcmp(pattern[k], pattern[q-1]):
            k += 1

        prefixFn[q-1] = k

    # Return the generated prefix function
    return prefixFn


# Testing

string1 = String('-ababaababaca')
pattern1 = String('ababaca')
alphabet1 = String('cba')

print('----findBiggestPrefix----')
print(findBiggestPrefix(string1, String('ba')))
print(findBiggestPrefix(string1, String('bac')))
print(findBiggestPrefix(string1, String('baca')))
print(findBiggestPrefix(string1, String('bacas')))
print(findBiggestPrefix(string1, String('vacas')))

print('\n----Matchers----')

print(f'Using Rabin Karp. Pattern starts at {RK_matcher(string1, pattern1)}')


statesArr = FA_computeTransition(pattern1, alphabet1)
print(
    f'Using Finite Automata. Pattern starts at {FA_matcher(string1, statesArr, len(pattern1))}')


print(f'Using KMP. Pattern starts at {KMP_matcher(string1, pattern1)}')
