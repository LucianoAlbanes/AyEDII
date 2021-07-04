# Part 2 of 'Análisis y Diseño de Algoritmos'
# Greedy

from lib.algo1 import *
from lib import linkedlist as LL

# Exercise 5

def adminActividades(tasks, start, end):
    '''
    Explanation:
        Select the largest possible set of activities that do not overlap and optimize the use of the resource
    Parameters:
        tasks: An array with tuples of each task (start, end).
        start: Positive integer that represents since when the common resource is available.
        end: Positive integer representing how long the common resource is available.
    Return:
        A LinkedList, with the maximum amount of task that not overlap.
    '''
    # Sort the tasks by execution time
    tasks = sortTasksByTime(tasks)

    # Define a list to save the tasks that will be executed
    confirmedTasks = LL.LinkedList()

    # Try to add tasks without overlaping
    for i in range(len(tasks)):
        start_i, end_i = tasks[i]
        if start_i >= start and end_i <= end:
            overlap = False
            actualNode = confirmedTasks.head

            while not overlap and actualNode:
                start_a, end_a = actualNode.value
                if not (end_i <= start_a or start_i >= end_a):
                    overlap = True
                actualNode = actualNode.nextNode

            if not overlap:
                LL.add(confirmedTasks, tasks[i])

    return confirmedTasks


def sortTasksByTime(array):
    '''
    Returns a new array with the tasks sorted in ascending order, in function to the time that requieres each.
    '''
    # Define a new array and copy elements
    outputArray = Array(len(array), (0, 0))
    for i in range(len(array)):
        outputArray[i] = array[i]

    # Sort (time betwen start and end values) (insertion sort)
    for i in range(1, len(outputArray)):
        temp = outputArray[i]
        temp_start, temp_end = temp
        tempTime = temp_end - temp_start

        j = i-1
        actual = outputArray[j]
        actual_start, actual_end = actual
        actualTime = actual_end - actual_start

        while j >= 0 and tempTime < actualTime:
            outputArray[j + 1] = outputArray[j]
            j -= 1
            actual = outputArray[j]
            actual_start, actual_end = actual
            actualTime = actual_end - actual_start
        outputArray[j + 1] = temp

    # Return the new sorted array
    return outputArray


# TEST (from https://ibb.co/yfwcH64)
tasks = Array(9, (0, 0))
tasks.data = [(1, 3), (1, 8), (2, 5), (4, 7), (5, 9),
              (8, 10), (9, 11), (11, 14), (13, 16)]

# taskSorted = [(1, 3), (8, 10), (9, 11), (2, 5), (4, 7), (11, 14), (13, 16), (5, 9), (1, 8)]

taskToDo = adminActividades(tasks, 0, 16)

actualTask = taskToDo.head
while actualTask:
    print(actualTask.value, end=', ')
    actualTask = actualTask.nextNode