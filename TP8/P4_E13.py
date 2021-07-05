# Part 3 of 'Análisis y Diseño de Algoritmos'
# Dynamic programming

from lib.algo1 import *


# Exercise 13


def canSumSet(setNum, number):
    # Define useful values
    numsQuant = len(setNum)

    # Define the array (boolean)
    canSumArray = Array(numsQuant+1, Array(number+1, False))

    # Calc values of the array
    # Make subsets smaller and check what values they can reach as a sum.
    # Verify with Dynamic programming if the current subset can reach the sum, with prev values or prev + actual

    # Init values, first column (sum == 0)
    for i in range(numsQuant+1):
        canSumArray[i][0] = True

    # Init values, first row (empty set)
    for i in range(1, number+1):
        canSumArray[0][i] = False

    # Calc the rest of the subsets if reach each sum
    for actualNum in range(1, numsQuant+1):
        for actualSum in range(1, number+1):

            # Get previous number value
            previous = canSumArray[actualNum-1][actualSum]

            if actualSum < setNum[actualNum-1]:
                # The num to insert is bigger, check what happend previously (set w/o actualNum)
                canSumArray[actualNum][actualSum] = previous

            else:
                # The actualNum could reach the actual sum, verify if was previously reached or
                # substract the actualNum to the actualSum and verify if is True
                substracting = canSumArray[actualNum - 1][actualSum-setNum[actualNum-1]]
                canSumArray[actualNum][actualSum] = (previous or substracting)

    # Return the result boolean value of the biggest sum (number parameter) and set containing all numbers (setNum parameter)
    return canSumArray[numsQuant][number]


# TEST
print(canSumSet([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 50))
print(canSumSet([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 500))
