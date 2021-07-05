# Part 1 of 'Análisis y Diseño de Algoritmos'
# Backtracking

from lib.algo1 import *
from lib.sortArray import insertionSortR as sort

# Exercise 1

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
    # Sort coins (Descending)
    coins = sort(coins)

    # Declare a variable to store the best case (min depth)
    bestDepth = None

    # Recursively start with depth 0 (initial depth, no coins)
    offset = startCoin(change, coins)
    for i in range(offset, len(coins)):
        # 0 is hardcoded, because this is the first depth
        if not bestDepth or bestDepth > 1:
            result = darCambioBacktrack(
                change, i, coins, 0, bestDepth, i-offset)
            if result:
                bestDepth = result

    # Return the minimun amount of coins (min depth)
    return bestDepth


def darCambioBacktrack(residue, coinIndex, coinsArray, actualdepth, bestDepth, skipCoins):
    '''
    Explanation:
        Recursive aux function of darCambio()
    Parameters:
        residue: Remaining amount to reach.
        coinIndex: The index of the coin corresponding to the current call.
        coinsArray: The array with the denominations of each coin.
        actualDepth: The depth of the current call.
        bestDepth: The actual minimun amount of coins already discovered to reach the change.
        skipCoins: The amount of the already checked coins, (Prevent permutations).
    '''
    # Compute current state (call) values
    residue -= coinsArray[coinIndex]
    actualdepth += 1

    # Verify cases
    if residue == 0:  # Exact amount
        bestDepth = actualdepth
    elif residue > 0 and (not bestDepth or bestDepth > actualdepth+1):
        # Set parameters
        offset = startCoin(residue, coinsArray)
        start = biggest(offset, (skipCoins-1))

        # Continue recursively
        for i in range(start, len(coinsArray)):
            if not bestDepth or bestDepth > actualdepth+1:
                result = darCambioBacktrack(
                    residue, i, coinsArray, actualdepth, bestDepth, i-start)
                if result:
                    bestDepth = result
    # Return the bestDepth (could be the same as parameter or newer)
    return bestDepth


def startCoin(change, coins):
    # This function returns an integer, indicating the first coin that is less or equal than the given change
    # Usefull to only verify coins that can be used
    i = 0
    length = len(coins)
    while i < length and coins[i] > change:
        i += 1
    return i


def biggest(a, b):
    # Return the biggest integer
    result = a
    if b > a:
        result = b
    return result


print(darCambio(14, [1, 2, 8, 6, 10]))
print(darCambio(109, [1, 6, 9, 4, 16]))
