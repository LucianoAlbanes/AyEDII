# Part 3 of 'Análisis y Diseño de Algoritmos'
# Divide and conquer

from lib.algo1 import Array
from P3_E9 import divideBK
import math

# Exercise 11


def contiguoMediana(numberList, k):
    # Define variables
    result = None
    length = len(numberList)
    posMedian = math.floor(length/2)
    k_low = math.floor(k/2)
    k_high = math.ceil(k/2)

    # Move the median to the middle
    divideBK(numberList, 0, length-1, posMedian)

    # Move the adjacent k/2 values next to median
    # (with divideBk, move elements median+-k/2-1)
    if posMedian-k_low-1 > 0:
        divideBK(numberList, 0, posMedian-1, posMedian-k_low-1)
    if posMedian+k_high+1 < length:
        divideBK(numberList, posMedian+1, length-1, posMedian+k_high+1)

    # Define result array
    result = Array(k, 0)

    for i in range(0, k):
        if i-k_low < 0:
            result[i] = numberList[posMedian-k_low+i]
        else:
            result[i] = numberList[posMedian-k_low+i+1]

    # Return the result
    return result


# TEST
import random
a = []

for i in range(100_000):
    a.append(random.randint(0, 1_000_000))

print(contiguoMediana(a, 10))

a.sort()
print(a[50_000])
