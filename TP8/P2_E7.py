# Part 2 of 'Análisis y Diseño de Algoritmos'
# Greedy

from lib.algo1 import *
from lib import linkedlist as LL

# Exercise 7


def mochila(maxWeight, cansArray):
    '''
    Explanation:
        Finds the best arraignments of cans to reach the maximum possible profit
        without sobrepassing a given weight.
    Parameters:
        maxWeight: The maximum amount of weight that the backpack can carry.
        cansArray: An array with the weights and profit of each can as tuple (weight, profit).
    Return:
        An array with the cans that maximize the profit in the backpack.
    '''
    # Define result variable
    result = None

    # Sort the cans by the ratio weight/profit
    cansByRatio = sortCansByRatio(cansArray)

    # Fill the bag while are space left with the cans with best ratio first (Greedy)
    selectedCansIndex = LL.LinkedList()
    leftWeight = maxWeight

    for i in range(len(cansByRatio)):
        actual_weight, _ = cansByRatio[i]

        if leftWeight > 0 and actual_weight <= leftWeight:
            LL.add(selectedCansIndex, i)
            leftWeight -= actual_weight

    # Create the result array with the selected cans (if are)
    # Dump the lineked list into the array
    if selectedCansIndex.head:
        length = LL.length(selectedCansIndex)
        result = Array(length, (0, 0))

        actualCanIndex = selectedCansIndex.head
        for i in range(length):
            result[i] = cansByRatio[actualCanIndex.value]
            actualCanIndex = actualCanIndex.nextNode

    # Return the result
    return result


def sortCansByRatio(array):
    '''
    Returns a new array with the cans sorted in ascending order in function to the ratio weight/profit.
    '''
    # Define a new array and copy elements
    outputArray = Array(len(array), (0, 0))
    for i in range(len(array)):
        outputArray[i] = array[i]

    # Sort (Insertion Sort)
    for i in range(1, len(outputArray)):
        temp = outputArray[i]
        temp_weight, temp_profit = temp
        tempRatio = temp_weight/temp_profit

        j = i-1
        actual = outputArray[j]
        actual_weight, actual_profit = actual
        actualRatio = actual_weight/actual_profit

        while j >= 0 and tempRatio < actualRatio:
            outputArray[j + 1] = outputArray[j]
            j -= 1
            actual = outputArray[j]
            actual_weight, actual_profit = actual
            actualRatio = actual_weight/actual_profit
        outputArray[j + 1] = temp

    # Return the new sorted array
    return outputArray


# Test
cans = [(24, 24), (10, 18), (10, 18), (7, 10)]

cansArr = Array(len(cans), (0, 0))
cansArr.data = cans

selectedCans = mochila(25, cansArr)
print(selectedCans)
