# Part 1 of 'Análisis y Diseño de Algoritmos'
# Backtracking

from lib.algo1 import *
from lib.sortArray import insertionSortR as sort

# Exercise 4

'''

Dado un array X de números enteros positivos y un número entero de T, implementar un algoritmo
que devuelva si existe un subconjunto de elementos en X que suman el valor T. Por ejemplo si X = {8, 6, 7, 5, 3, 10, 9} y T = 15,
la respuesta es True, porque los subconjuntos {8, 7} , {7, 5, 3} , {6, 9} , {5,10}
todos suman 15. Con este otro ejemplo X = {11, 6, 5, 1, 7, 13, 12} y T = 15, la respuesta es False.

    def subconjuntoSuma(numeros, valor):
    Descripción: Implementa la función Subconjunto Suma
    Entrada: numeros array de enteros positivos, valor entero positivo.
    Salida: retorna True si existe un grupo de enteros en números cuya
    suma del valor de entrada.

'''


def subconjuntoSuma(numbersArray, value):
    '''
    Explanation:
        Finds if a given value can be expressed as the sum of some values (positives integers) of an array.
    Parameters:
        numbersArray: An array with the values.
        maxWeight: The value to be reached.
    Return:
        A boolean value. 'True' if there is a group of integers whose sum is the input value. Otherwise, 'False'.
    '''
    # Sort elements (Descending)
    numbersArray = sort(numbersArray)

    # Declare a variable to store the result
    result = False  # Is false until proven otherwise

    # Start recursion
    offset = startNum(value, numbersArray)
    for i in range(offset, len(numbersArray)):
        # The second comparison verify that is possible to get the value
        # if the bigger reamaining number * remaining values is less than value, can't reach
        if not result and numbersArray[i]*(len(numbersArray)-i) >= value:
            result = subconjuntoSumaBacktrack(value, i, numbersArray, i-offset)

    # Return the result (boolean value)
    return result


def subconjuntoSumaBacktrack(residue, actualValue, remainingValues, skipValues):
    '''
    Explanation:
        Recursive aux function of subconjuntoSuma()
    Parameters:
        residue: Remaining value to reach.
        actualValue: The index of the number to be checked.
        remainingValues: The array that contains all the remaining integers.
        skipValues: The amount of the already checked coins, (Prevent permutations).
    '''
    # Compute current state (call) values
    residue -= remainingValues[actualValue]
    result = False

    # Verify cases
    if residue == 0:  # Base case
        result = True
    elif residue > 0:  # General case
        # Remove the recently added value from the array
        remainingValues = subArray(remainingValues, actualValue)

        # Set parameters
        offset = startNum(residue, remainingValues)
        start = biggest(offset, (skipValues-1))

        # Continue recursively
        for i in range(start, len(remainingValues)):
            if not result and remainingValues[i]*(len(remainingValues)-i) >= residue:
                result = subconjuntoSumaBacktrack(
                    residue, i, remainingValues, i-start)

    # Return the result (boolean value)
    return result


def startNum(left, numbersArray):
    # This function returns an integer, indicating the first element that is less or equal to the reaming amount
    # Usefull to only verify numbers that can be used.
    i = 0
    length = len(numbersArray)
    while i < length and numbersArray[i] > left:
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
print(subconjuntoSuma([8, 6, 7, 5, 3, 10, 9], 15))
print(subconjuntoSuma([11, 6, 5, 1, 7, 13, 12], 15))
