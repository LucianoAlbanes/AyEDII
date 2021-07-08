# Part 2 of 'Análisis y Diseño de Algoritmos'
# Greedy

from lib.algo1 import *
from lib.sortArray import insertionSortR as sort

# Exercise 6


def buscarPares(array):
    '''
    Explanation:
        Creates pairs of numbers such that the maximum value of the sums
        of the numbers of each pair is as small possible.
    Parameters:
        array: Array of a even quantity of integers.
    Return:
        Returns the value of the largest sum resulting from the pairs.
    '''
    # Define a result variable
    result = None

    # Verify that the amount of values of array is even and continue
    if (len(array) % 2) == 0:
        # Sort the array
        array = sort(array)

        # Search for the max sum value
        length = len(array)
        for i in range(0, length, 2):
            sum = array[i] + array[length-i-1]
            if not result or sum > result:
                result = sum
    
    # Return the result, (None if array length is odd)
    return result

arr = [5,8,1,4,7,9]
print(buscarPares(arr))