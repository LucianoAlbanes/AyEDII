# Part 1 of 'Análisis y Diseño de Algoritmos'
# Backtracking

# Exercise 1
'''
Implementar la función Dar Cambio que devuelve la cantidad mínima de monedas que hay que dar
para cambiar n pesos con monedas de la denominación dada como parámetro.
    def darCambio(Cambio, Monedas)
    Descripción: Implementa la operación devolver cambio
    Entrada: Cambio número que representa el monto del cambio, Monedas, un
    Array con las monedas que se dispone para dar ese cambio.
    Salida: retorna el número mínimo de monedas que son utilizadas para
    devolver el cambio.
Nota: Asuma que en la lista de monedas siempre está la moneda con valor 1. Y que las monedas no
se agotan.
Ejemplos:
        monedas = [1, 2, 6, 8, 10], cambio = 14, solución: 2 (una moneda con denominación 6 y otra con 8)
        monedas = [1, 3, 11, 7, 12], cambio = 20, solución: 3 (utilizando la combinación de monedas 12,7,1)
'''
from lib.algo1 import *
from lib.sortArray import insertionSort as sort
monedas = Array(8, 0)
monedas.data = [10, 12, 13, 33, 42, 100, 140, 999]

count = 0
def darCambio(change, coins):
    # Sort coins
    coins = sort(coins) # Implementar


    bestCase = None #  Min amount of coins

    # Start recursion, initDepth=0 (depth == amount of coins)
    for i in range(len(coins)):
        # Verify that the coins are not larger than change
        if change < coins[i]:
            break
        else:
            currentCase = darCambioRecursive(change, i, 0, bestCase, coins)
            if not bestCase or (currentCase and currentCase < bestCase):
                bestCase = currentCase

    # Return the bestCase (Minor depth with no residue)
    return bestCase


def darCambioRecursive(residue, actualCoin, depth, bestCase, coins):
    # Update actual level
    depth += 1
    residue -= coins[actualCoin]
    global count
    count +=1
    # Verify
    result = None
    if not bestCase or depth < bestCase:
        if residue == 0:
            result = depth
        elif residue > 0:
            # Go deeper
            for i in range(len(coins)):
                # Verify that the coins are not larger than change
                if residue < coins[i]:
                    break
                else:
                    recursionReturn = darCambioRecursive(
                        residue, i, depth, bestCase, coins)
                    if recursionReturn != None:
                        result = recursionReturn
                        bestCase = result
    #
    return result

#
print(darCambio(578, monedas))
print(count)
