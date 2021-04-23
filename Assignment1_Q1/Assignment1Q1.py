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

def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left)
        mergeSort(right)

        x = 0
        y = 0
        z = 0

        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                array[z] = left[x]
                x = x + 1
            else:
                array[z] = right[y]
                y = y + 1
            z = z + 1
        
        while x < len(left):
            array[z] = left[x]
            x = x + 1
            z = z + 1
        
        while y < len(right):
            array[z] = right[y]
            y = y + 1
            z = z + 1
        

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
        mergeSort(tempArray)
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
        mergeSort(tempArray)
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
