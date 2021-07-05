# Part 3 of 'Análisis y Diseño de Algoritmos'
# Dynamic programming

from lib.algo1 import *
from lib.sortArray import insertionSort as sort
# We assume that the coin of value 1 exists in the array. We could use math.Inf in the case that isn't possible to give change

# Exercise 12


def darCambio(change, coins):
    '''
    Explanation:
        Returns the minimum amount of coins to be given to reach a specified amount of pesos.
    Info:
        The supply of coins are unlimited, and the coin of value 1 will be into the coins array.
    Parameters:
        change: The amount of pesos to be reached.
        coins: An array with the denominations of each coin.
    Return:
        An integer with the minimun amount of coins, 'None' if is not possible.
    '''
    # Sort coins (Ascending)
    coins = sort(coins)

    # Define useful values
    coinsQuant = len(coins)

    # Define the array
    changeArray = Array(coinsQuant, Array(change+1, 0))

    # Fill case coin of value 1
    for i in range(change+1):
        changeArray[0][i] = i

    # Rest of coins
    for actualCoin in range(1, coinsQuant):
        for actualChange in range(change+1):
            usingPrevCoins = changeArray[actualCoin-1][actualChange]
            usingActualCoin = changeArray[actualCoin][(actualChange % coins[actualCoin])]

            if usingActualCoin != None:
                usingActualCoin += int(actualChange/coins[actualCoin])
                changeArray[actualCoin][actualChange] = minimum(
                    usingActualCoin, usingPrevCoins)
            else:
                changeArray[actualCoin][actualChange] = usingPrevCoins


    # Return the amount of coins needeed for the given change
    return changeArray[coinsQuant-1][change]


def minimum(a, b):
    # Return the minimun integer
    result = a
    if b < a:
        result = b
    return result

# Tests
print(darCambio(8, [1, 4, 6]))
print(darCambio(14, [1, 2, 8, 6, 10]))
print(darCambio(109, [1, 6, 9, 4, 16]))
