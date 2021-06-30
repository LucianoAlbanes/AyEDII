'''

Implementar la función Subsecuencia Creciente que devuelva un array con la mayor cantidad de elementos
del array de entrada que formen una secuencia monótona creciente.
Los elementos en el resultado deben aparecer en el mismo orden en que aparecían en el array de entrada,
y no tienen que ser consecutivos dentro de este.
Por ejemplo, la mayor subsecuencia creciente en [5, 1, 2, 3, 100, 20, 17, 8, 19, 21] es [1, 2, 3, 8, 19, 21]. 

def subsecuenciaCreciente(numeros): 
Descripción: Implementa la función SubsecuenciaCreciente 
Entrada: numeros array de números naturales.
Salida: retorna array de números con la mayor subsecuencia creciente en el array de entrada numero.


'''
from lib.algo1 import *


def subsecuenciaCreciente(numbersArray):
    '''
    Explanation:
        Finds the largest sequence of numbers of the input array that form a
        monotonically increasing sequence(respecting the original order).
    Info:
        There may be multiple sequences that satisfy the requirements. Only one of them will be returned.
    Parameters:
        numbersArray: An array of integers to check.
    Return:
        An array with the largest sequence found.
    '''
    # Define a result variable and call the backtrack function with the start values
    resultArray = subsecuenciaCrecienteBacktrack(
        None, 0, numbersArray, len(numbersArray), 0)
    
    # Return the array with the largest subsequence
    return resultArray


def subsecuenciaCrecienteBacktrack(previous, actual, numbersArray, length, depth):
    '''
    Explanation:
        Recursive aux function of subsecuenciaCreciente()
    Parameters:
        previous: The index where is located the current max number of the sequence.
        actual: The index of the number to be checked.
        numbersArray: The original array that contains all the integers.
        length: The length of numbersArray.
        depth: How many items contain the actual subsequence.
    '''
    # Cases
    if actual >= length:  # Base case
        result = Array(depth, 0)

    elif previous != None and numbersArray[previous] >= numbersArray[actual]:  # Minor number, continue backtrack actual++
        result = subsecuenciaCrecienteBacktrack(
            previous, actual+1, numbersArray, length, depth)
    else: #  Bigger number appears, two options, use it and continue recursively or ignore and keep the previous.
        useCase = subsecuenciaCrecienteBacktrack(
            actual, actual+1, numbersArray, length, depth+1)
        ignoreCase = subsecuenciaCrecienteBacktrack(
            previous, actual+1, numbersArray, length, depth)
        # Choose the bigger subsequence obtained.
        result = biggestArr(useCase, ignoreCase)

    # Update the value of result array with current depth
    if not actual > length and previous != None:
        result[depth-1] = numbersArray[previous]
    
    # Return the result array
    return result


def biggestArr(arrA, arrB):
    # Return the biggest (size) array
    result = arrA
    if len(arrB) > len(arrA):
        result = arrB
    return result



######### TEST
print(subsecuenciaCreciente([5, 1, 2, 3, 100, 20, 17, 8, 19, 21])) # Returns [1, 2, 3, 8, 19, 21] or [1, 2, 3, 17, 19, 21]

import random
for i in range(100):
    print('\n')
    arr = []
    for j in range(random.randint(10,25)):
        arr.append(random.randint(0,100))
    print(arr)
    print(subsecuenciaCreciente(arr))