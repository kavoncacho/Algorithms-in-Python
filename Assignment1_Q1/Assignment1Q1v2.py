from random import randint
from random import randrange
import time
import re
import sys
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

sys.setrecursionlimit(1500)
try:
    arrayLength = int(input("Please input the size of the array (Reccomended 150): "))
except ValueError:
    print("That was not an integer. Please run the program again.")
    quit()

"""
for testing purposes
array = [randrange(0,1000) for x in range(arrayLength)]
print ("")
for x in array:
    print(x)
print ("")
"""

print("\nA - Insertion sort \nB - Merge sort \nC - Both")
choice = input("\nPlease select which method you'd like to run: ")
print("")

def insertionSort(array):
    start = time.time()
    for x in range(1, len(array)):
        key = array[x]
        y = x - 1
        while y >= 0 and key < array[y]:
            array[y + 1] = array[y]
            y = y - 1
        array[y + 1] = key
    end = time.time()
    return (end - start) * 1000

def mergeSort(array, left, right):
    if left >= right:
        return
    
    mid = (left + right)//2
    mergeSort(array, left, mid)
    mergeSort(array, mid + 1, right)
    mergeSortHelper(array, left, right, mid)

def mergeSortHelper(array, left, right, mid):
    leftArray = array[left:mid + 1]
    rightArray = array[mid + 1:right + 1]

    leftArrayIndex = 0
    rightArrayIndex = 0
    sortedIndex = left

    while leftArrayIndex < len(leftArray) and rightArrayIndex < len(rightArray):
        if leftArray[leftArrayIndex] <= rightArray[rightArrayIndex]:
            array[sortedIndex] = leftArray[leftArrayIndex]
            leftArrayIndex = leftArrayIndex + 1
        else:
            array[sortedIndex] = rightArray[rightArrayIndex]
            rightArrayIndex = rightArrayIndex + 1

        sortedIndex = sortedIndex + 1

    while leftArrayIndex < len(leftArray):
        array[sortedIndex] = leftArray[leftArrayIndex]
        leftArrayIndex = leftArrayIndex + 1
        sortedIndex = sortedIndex + 1

    while rightArrayIndex < len(rightArray):
        array[sortedIndex] = rightArray[rightArrayIndex]
        rightArrayIndex = rightArrayIndex + 1
        sortedIndex = sortedIndex + 1
        

if choice == 'A':
    save = input('Would you like to save the plot? (Y/N): ')
    print('Close the pop-up window to quit the program.\n')
    x = 0
    array = [randrange(0,1000) for arrayLength in range(arrayLength)]
    nArray = [0] * arrayLength
    timeArray = [0] * arrayLength
    nArray = range(0, arrayLength)
    fig, ax = plt.subplots()
    while x < int(arrayLength):
        y = 0
        tempArray = [0] * (x + 1)
        while y <= x:
            tempArray[y] = array[y]
            y = y + 1
        time1 = insertionSort(tempArray)
        timeArray[x] = time1
        x = x + 1
    ax.plot(nArray, timeArray)
    ax.set_xlabel('n')
    ax.set_ylabel('T (ms)')
    ax.set_title("Insertion Sort")
    ax.autoscale()
    if save == 'Y':
        fig.savefig("InsertionSort.png")
        plt.show()
    else:
        plt.show()
    
elif choice == 'B':
    save = input('Would you like to save the plot? (Y/N): ')
    print('Close the pop-up window to quit the program.\n')
    x = 0
    array = [randrange(0,1000) for arrayLength in range(arrayLength)]
    nArray = [0] * arrayLength
    timeArray = [0] * arrayLength
    nArray = range(0, arrayLength)
    fig, ax = plt.subplots()
    while x < int(arrayLength):
        y = 0
        tempArray = [0] * (x + 1)
        while y <= x:
            tempArray[y] = array[y]
            y = y + 1
        start1 = time.time()
        mergeSort(tempArray, 0, len(tempArray) - 1)
        end1 = time.time()
        time1 = ((end1 - start1) * 1000)
        timeArray[x] = time1
        x = x + 1
    ax.plot(nArray, timeArray)
    ax.set_xlabel('n')
    ax.set_ylabel('T (ms)')
    ax.set_title("Merge Sort")
    ax.autoscale()
    if save == 'Y':
        fig.savefig("Merge.png")
        plt.show()
    else:
        plt.show()
elif choice == 'C':
    save = input('Would you like to save the plot? (Y/N): ')
    print('Close the pop-up window to quit the program.\n')
    x = 0
    array = [randrange(0,1000) for arrayLength in range(arrayLength)]
    nArray = [0] * arrayLength
    iTimeArray = [0] * arrayLength
    mTimeArray = [0] * arrayLength
    nArray = range(0, arrayLength)
    fig, ax = plt.subplots()
    while x < int(arrayLength):
        y = 0
        tempArray = [0] * (x + 1)
        while y <= x:
            tempArray[y] = array[y]
            y = y + 1
        time1 = insertionSort(tempArray)
        iTimeArray[x] = time1
        start2 = time.time()
        mergeSort(tempArray, 0, len(tempArray) - 1)
        end2 = time.time()
        time2 = ((end2 - start2) * 1000)
        mTimeArray[x] = time2
        x = x + 1
    ax.plot(nArray, iTimeArray, label = 'Insertion')
    ax.plot(nArray, mTimeArray, label = 'Merge')
    ax.set_xlabel('n')
    ax.set_ylabel('T (ms)')
    ax.set_title("Insertion Sort vs. Merge Sort")
    ax.autoscale()
    ax.legend()
    if save == 'Y':
        fig.savefig("InsertionVersusMerge.png")
        plt.show()
    else:
        plt.show()
else:
    print("That is not the choice. Please run the program again.")
