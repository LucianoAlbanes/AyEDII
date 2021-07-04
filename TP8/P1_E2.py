# Part 1 of 'Análisis y Diseño de Algoritmos'
# Backtracking

from lib.algo1 import *
from lib.sortArray import insertionSortR as sort

# Exercise 2

def mochila(maxWeight, cansArray):
    '''
    Explanation:
        Finds the best arraignments of cans to reach the maximum possible weight.
    Parameters:
        maxWeight: The maximum amount of weight that the backpack can carry.
        cansArray: An array with the weights of each can.
    Return:
        An array with the cans that maximize the weight in the backpack.
    '''
    # Sort cans weight (Descending)
    cansArray = sort(cansArray)

    # Declare a variable to store the min remaining weight reached
    minRemainingWeight = None

    # Result array of cans
    resultArray = None

    # Recursively start with depth 0 (initial depth, no coins)
    offset = startCan(maxWeight, cansArray)
    for i in range(offset, len(cansArray)):
        depth = 0
        if minRemainingWeight == None or minRemainingWeight > 0:  # If ==0, max weight reached
            result = mochilaBacktrack(
                maxWeight, i, cansArray, depth, minRemainingWeight, i-offset)
            if result[0]:
                # Get a array
                resultArray, minRemainingWeight = result
                resultArray[depth] = cansArray[i]

    # Return the minimun amount of coins (min depth)
    return resultArray


def mochilaBacktrack(leftWeight, actualCan, cansArray, depth, minRemainingWeight, skipCans):
    '''
    Explanation:
        Recursive aux function of mochila()
    Parameters:
        leftWeight: Remaining weight avaible .
        actualCan: The index of the can corresponding to the current call.
        cansArray: The array with the remaining cans.
        depth: The depth of the current call.
        minRemainingWeight: The minimum weight residue already reached.
        skipCans: The amount of the already checked cans, (Prevent permutations).
    '''
    # Result array of cans
    resultArray = None

    # Compute current state (call) values
    leftWeight -= cansArray[actualCan]
    depth += 1

    # Verify cases
    if minRemainingWeight == None or minRemainingWeight > 0:
        remainingCansArray = subArray(cansArray, actualCan)
        offset = startCan(leftWeight, remainingCansArray)
        start = biggest(offset, (skipCans-1))

        # Try to continue deeper, otherwise save this arraignment
        if leftWeight > 0 and start != len(remainingCansArray):
            # Continue deeper, the array has remaining cans
            for i in range(start, len(remainingCansArray)):
                if minRemainingWeight == None or minRemainingWeight > 0:  # If ==0, max weight reached
                    result = mochilaBacktrack(
                        leftWeight, i, remainingCansArray, depth, minRemainingWeight, i-start)
                    if result[0]:
                        resultArray, minRemainingWeight = result
                        resultArray[depth-1] = cansArray[actualCan]
        else:
            # Can't go deeper, min value reached.
            if minRemainingWeight == None or leftWeight < minRemainingWeight:
                minRemainingWeight = leftWeight
                resultArray = Array(depth, 0)
                resultArray[depth-1] = cansArray[actualCan]

    # Return the result of the array of cans, can be None (nothing found), or an array with some cans
    return resultArray, minRemainingWeight


def startCan(leftWeight, cansArray):
    # This function returns an integer, indicating the first can that is less or equal to the reaming weight
    # Usefull to only verify cans that can be used
    i = 0
    length = len(cansArray)
    while i < length and cansArray[i] > leftWeight:
        i += 1
    return i


def subArray(array, index):
    '''
    Explanation:
        Creates a new array, without one element (index)
    Parameters:
        array: The original array
        index: The position where is the element to be removed
    Return:
        A new array, w/o that element and length-1.
    '''
    newArray = Array(len(array)-1, array[0])  # array[0] to match elements type

    # Elements before index
    for i in range(index):
        newArray[i] = array[i]

    # Elements after index
    for i in range(index, len(newArray)):
        newArray[i] = array[i+1]

    # Return the new array
    return newArray


def biggest(a, b):
    # Return the biggest integer
    result = a
    if b > a:
        result = b
    return result


# Test
cans = [50, 90, 122, 534, 123, 11, 33, 3, 10, 10]

cansArr = Array(len(cans), 0)
cansArr.data = cans

print(sort(cans))
print(mochila(69, cansArr))
