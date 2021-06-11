# Implementation of patter matching exercises
# Part 2 of Pattern Matching
from lib.algo1 import *
from lib import linkedlist as LL
from lib.hashLinear import hashLinear as h


# Rabin Karp

# Finite automata

def FA_matcher(string, statesArray, finalState):
    currentState = 0
    lengthAlphabet = len(statesArray[0])


    for i in range(len(string)):
        # Get index of character from the first row
        charIndex = h(ord(string[i]), statesArray[0], lengthAlphabet)

        if charIndex != None:  # Verify if is part of the alphabet
            currentState = statesArray[currentState+1][charIndex]
            if currentState == finalState:
                print(f'Pattern in string here: [{i-finalState+1}, {i}]')
                break
        else:
            # An unrecognized character appears, need to start from state 0
            currentState = 0


def FA_computeTransition(pattern, alphabet):
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


p1 = String('ababaca')
a1 = String('cba')
A = FA_computeTransition(p1, a1)
for e in A:
    print(e)
FA_matcher('-ababaababaca', A, 7)

# Knuth Morris Pratt
