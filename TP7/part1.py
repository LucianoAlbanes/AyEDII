# Implementation of patter matching exercises
# Part 1 of Pattern Matching
from lib.algo1 import *
from lib import mydictionaryChar as D
from lib import linkedlist as LL


# Define functions


def existChar(string, character):
    '''
    Explanation: 
        Checks if a given character exists in a given string.
    Params:
        string: The string where will be checked the existence of the character.
        character: The character to be searched.
    Return:
        A boolean value, 'True' if the character exists in the string, 'False' otherwise.
    '''
    # Define flag
    found = False

    # Verify for the length of both inputs
    if not (len(character) != 1 and len(string) < 1):
        # Compare each character of string with the given character
        for i in range(len(string)):
            if strcmp(string[i], character):
                # Found!
                found = True
                break

    # Return the result
    return found


def isPalindrome(string):
    '''
    Explanation: 
        Checks if a given string is a palindrome.
    Params:
        string: The string to be checked.
    Return:
        A boolean value, 'True' if the string is palindrome, otherwise 'False'.
    '''
    # Define flag
    isPalindromeFlag = True

    # Verify (is palindrome until proven otherwise)
    length = len(string)
    for i in range(int(length/2)):  # Int() as floor
        if not strcmp(string[i], string[length-i-1]):
            # Oops...
            isPalindromeFlag = False
            break

    # Return the result
    return isPalindromeFlag


def mostRepeatedChar(string):
    '''
    Explanation: 
        Finds the most repeated character in a given string.
    Params:
        string: The string to be checked.
    Return:
        The character with most ocurrences.
        In case there is more than one character that satisfy the criteria, returns the first of them.
    '''
    # Creates a hash table to store how many times each character apears in the string
    dictionary = Array(16, LL.LinkedList())

    # Define a variable to store the current most repeated character, and loop the string.
    # The first character will be the first mostRepeated char:
    D.insert(dictionary, string[0], 1)
    mostRepeated = D.getNodeByKey(
        dictionary[D.h(string[0], len(dictionary))], string[0])

    for i in range(1, len(string)):
        # Get node of actualCharacter
        actualChar = D.getNodeByKey(
            dictionary[D.h(string[i], len(dictionary))], string[i])

        # Check if exist to compare, otherwise add it.
        if actualChar:
            # Exists. Increment, compare with actual mostRepeated
            actualChar.value += 1
            if actualChar.value > mostRepeated.value:
                mostRepeated = actualChar
        else:
            # Not exists, add with value 1 into the hash table
            indexSlot = D.h(string[i], len(dictionary))
            if not dictionary[indexSlot]:
                dictionary[indexSlot] = LL.LinkedList()

            # Add the new node to the list
            D.add(dictionary[indexSlot], string[i], 1)

    # Return the character with most ocurrences
    return mostRepeated.key


def getBiggestIslandLen(string):
    '''
    Explanation: 
        Finds the 'biggest island of characters' in a given string.
    Params:
        string: The string to be checked.
    Return:
        The size of the biggest island.
    '''
    # Define a variable to store te current max island size value.
    maxSize = 0

    # Verify length
    if len(string) > 0:
        maxSize = 1  # At least, one character

        # Loop the string, searching for bigger islands
        currentSize = 1
        for i in range(1, len(string)):
            # Search for biggest islands
            if strcmp(string[i-1], string[i]):
                currentSize += 1
                if currentSize > maxSize:
                    maxSize = currentSize
            else:
                # New character
                currentSize = 1

    # Return the value of the biggest island found
    return maxSize


def isAnagram(string1, string2):
    '''
    Explanation: 
        Compares if a string is an anagram (permutation) of another.
    Params:
        string1: The first string.
        string2: The second string.
    Return:
        'True' is string1 is an anagram of string2, otherwise 'False'.
    '''
    # Define result variable
    isPermutation = False

    # Check if the two str have same length. Otherwise is not a permutation.
    if len(string1) == len(string2):
        # Same length, compare using hash tables.
        # Now, isPermutation is true until proven otherwise.
        isPermutation = True

        # Define a dictionary to store each character of string1
        dictionary = Array(16, LL.LinkedList())
        for i in range(0, len(string1)):
            # Get node of actualCharacter
            actualChar = D.getNodeByKey(
                dictionary[D.h(string1[i], len(dictionary))], string1[i])

            # Check if exist to increment, otherwise add it.
            if actualChar:
                # Exists. Increment, compare with actual mostRepeated
                actualChar.value += 1
            else:
                # Not exists, add with value 1 into the hash table
                indexSlot = D.h(string1[i], len(dictionary))
                if not dictionary[indexSlot]:
                    dictionary[indexSlot] = LL.LinkedList()

                # Add the new node to the list
                D.add(dictionary[indexSlot], string1[i], 1)

        # Check existence and delete of each character of string2 in the created dictionary
        for i in range(len(string2)):
            # Get node of actualCharacter
            actualChar = D.getNodeByKey(
                dictionary[D.h(string2[i], len(dictionary))], string2[i])

            # Checks if exists to decrement, otherwise is not a permutation
            if actualChar and actualChar.value > 0:
                actualChar.value -= 1
            else:
                isPermutation = False
                break  # When a discrepancy appears, break the loop.

    # Return result
    return isPermutation


def verifyBalancedParentheses(string):
    '''
    Explanation: 
        Checks if the parentheses contained in a string are balanced and in order.
    Params:
        string: The string to be checked.
    Return:
        'True' if is the string is balanced and in order, otherwise 'False'
    '''
    # Define isBalanced flag.
    isBalanced = False

    # A 'balance' variable will be used to count the number of parenthesis.
    # '(' adds 1 to 'balance'
    # ')' removes 1 to 'balance'
    # 'balance' value can't be less than 0.
    # 'balance' value at the end of the string must be 0
    balance = 0
    openParenthesis = String('(')
    closeParenthesis = String(')')

    for i in range(len(string)):
        if strcmp(string[i], openParenthesis):
            balance += 1
        elif strcmp(string[i], closeParenthesis):
            balance -= 1
            if balance < 0:
                # Balance is less than 0, string can't be balanced.
                isBalanced = False
                break

    # Check if balance equals to 0
    if balance == 0:
        isBalanced = True

    # Return the final result
    return isBalanced


def reduceLen(string):
    '''
    Explanation: 
        Reduces the length of a string by iteratively removing repeated pairs of characters.
    Params:
        string: The string to be reduced.
    Return:
        The reduced string.
    '''
    # Define an output string
    outputString = String('')

    # Iterate the original string, compare pairs and concat to output.
    for i in range(0, len(string), 2):
        # Get pair of characters
        char1 = String(string[i])
        char2 = None
        if i+1 != len(string):  # length of string could be odd
            char2 = String(string[i+1])

        # Add to output, cases odd string and pair has different characters
        if not char2:
            outputString = concat(outputString, char1)
        elif not strcmp(char1, char2):
            toAdd = concat(char1, char2)
            outputString = concat(outputString, toAdd)

    # Return the resultant string
    return outputString


def isContained(string1, string2):
    '''
    Explanation: 
        Determines if a word is contained in another word (maintaining order).
    Params:
        string1: The string where will be searched for the string2.
        string2: The string to be found
    Return:
        'True' if string1 contains string2, otherwise 'False'
    '''
    # Define a result variable
    contained = False

    # Search for each character of string2 in string1
    # Verify lengths
    if len(string1) >= len(string2):
        charactersFound = 0
        actualChar = string2[0]
        for i in range(len(string1)):
            if strcmp(actualChar, string1[i]):
                charactersFound += 1
                if charactersFound == len(string2):
                    # All characters found
                    contained = True
                    break
                else:
                    # Update actualChar
                    actualChar = string2[charactersFound]

    return contained


def isPatternContained(string, patternString, wildcard):
    '''
    Explanation: 
        Determines if a pattern of characters consisting by fixed characters and wildcards is found in another string.
    Params:
        string: The string where the pattern will be searched
        pattern: The pattern string to be searched
        wildcard: The wildcard character inside pattern.
    Return:
        'True' if the pattern provided is in the string, otherwise 'False'.
    '''
    # Define the inner funcion skipWildcards
    def skipWildcards(patternIndex, patternString):
        '''
        This inner functions get an actual index and a pattern.
        Will try to skip wildcards from the given index to return the index of the next character to verify.
        If there is not left characters, will return 'None'.
        This 'None' is equivalent to say that the pattern was found in the string.
        '''
        if patternIndex < len(patternString): 
            while strcmp(patternString[patternIndex], wildcard):
                if patternIndex+1 < len(patternString):
                    patternIndex += 1
                else:
                    patternIndex = None  # All patterns found.
                    break
        else: # Overflow, pattern was entirely explored
            patternIndex = None
        return patternIndex

    # Define a result variable
    contained = False

    # Define indexes
    stringIndex = 0
    patternIndex = 0
    patternIndex = skipWildcards(patternIndex, patternString)

    # Search using Naive like algorithm
    if patternIndex != None: # Empty or pattern of only wildcards
        while not contained and stringIndex < len(string):
            current = 0
            while (stringIndex+current) < len(string) and strcmp(patternString[patternIndex+current], string[stringIndex+current]):
                # Match character found!. Increment current and verify if it's a end of pattern
                current += 1

                nextPatternIndex = skipWildcards((patternIndex+current), patternString)
                if nextPatternIndex == None:
                    # All patterns found!
                    contained = True
                    break
                elif nextPatternIndex > patternIndex+current:
                    # This pattern was complete, however, there is more patterns ahead.
                    stringIndex += current
                    patternIndex = nextPatternIndex
                    break

            # Increment start of string
            stringIndex += 1
    else:
        # No need to verify, it's True
        contained = True
    
    # Return the final result
    return contained


# TEST
if __name__ == "__main__":
    text1 = String('Hola buenas noches')
    print(existChar(text1, 'e'))

    text2 = String('anitalavalatina')
    print(isPalindrome(text2))

    text3 = ('Esta es una frase de ejemplo, hehehe.')
    print(mostRepeatedChar(text3))

    text4 = String('foobar')
    print(getBiggestIslandLen(text4))

    text5a = String('nacionalista')
    text5b = String('altisonancia')
    print(isAnagram(text5a, text5b))

    text6a = String('(ccc(ccc)cc((ccc(c))))')
    text6b = String(')ccc(ccc)cc((ccc(c)))(')
    print(verifyBalancedParentheses(text6a))
    print(verifyBalancedParentheses(text6b))

    text7 = String('aaabccddd')
    print(reduceLen(text7))

    text8a = String('aaafffmmmarillzzzllhooo')
    text8b = String('aaafffmmmarrrilzzzhooo')
    text8c = String('amarillo')
    print(isContained(text8a, text8c))
    print(isContained(text8b, text8c))

    text9a = String('cabccbacbacab')
    text9b = String('ab*ba*c')
    text9c = String('*')
    print(isPatternContained(text9a, text9b, text9c))
