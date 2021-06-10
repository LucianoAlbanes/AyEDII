# Implementation of patter matching exercises
# Part 2 of Pattern Matching
from lib.algo1 import *
from lib import linkedlist as LL


# Rabin Karp

# Finite automata

def FA_matcher(string, statesArray, finalState, alphabet):
    currentState = 0
    for i in range(len(string)):
        a = 0
        if string[i] == 'b': a=1
        if string[i] == 'c': a=2
        currentState = statesArray[currentState][a]
        if currentState == finalState:
            print(f'Pattern in string here: [{i-finalState}, {i}]')
            break



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

    # Define an array of |P|*|𝛴| to store the finite automata function
    FA_Function = Array(len(pattern), Array(len(alphabet), 0))
    
    # Find states (copy paste from CLRS)
    lengthP = len(pattern)
    for q in range(lengthP):
        for a in range(len(alphabet)):
            k = minimum((lengthP+1), (q+2))
            k -= 1
            while not isSuffix(substr(pattern, 0, k), concat(substr(pattern, 0, q), String(alphabet[a]))):
                k -= 1
            FA_Function[q][a] = k
    return FA_Function


p1 = String('ababaca')
a1 = String('abc')
A = FA_computeTransition(p1, a1)
for e in A:
    print(e)
FA_matcher('abbcbacbababcbabcabcbabcabcbacbababacaabcabcaabbabababababacaacaca', A, 7, a1)

# Knuth Morris Pratt
