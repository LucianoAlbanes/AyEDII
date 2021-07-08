# Part 4 of 'Análisis y Diseño de Algoritmos'
# Dynamic programming

from lib.algo1 import *

# Exercise 14

def mejorCamino(array):
    # Vars
    length = len(array)

    # Array path memo
    pathArray = Array(length, Array(length, 0))

    # Initialize array first row
    pathArray[0][0] = array[0][0]

    for i in range(1, length):
        pathArray[0][i] = pathArray[0][i-1] + array[0][i]
    
    # Initialize array first column
    for i in range(1, length):
        pathArray[i][0] = pathArray[i-1][0] + array[i][0]

    # Calc rest of array
    for i in range(1,length):
        for j in range(1, length):
            upValue = pathArray[i-1][j]
            leftValue = pathArray[i][j-1]

            # Save value
            if upValue < leftValue:
                pathArray[i][j] = upValue + array[i][j]
            else:
                pathArray[i][j] = leftValue + array[i][j]
    
    # Return the cost of the shortest path
    minCost = pathArray[length-1][length-1]

    return minCost




## TEST

A = Array(3, Array(3,0))

A[0].data = [1,2,3]
A[1].data = [3,5,6]
A[2].data = [0,1,1]



print(mejorCamino(A))