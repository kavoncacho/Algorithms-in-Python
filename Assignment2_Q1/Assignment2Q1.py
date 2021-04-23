from random import randint
from random import randrange
import math
import time
import re
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

sys.setrecursionlimit(1500)

try:
    arrayLength = int(input("Please input the size of the array: "))
except ValueError:
    print("That was not an integer. Please run the program again.")
    quit()



print("\nA - Brute Force \nB - Recursive Algorithms \nC - Both")
methodChoice = str(input("\nPlease choose the method if approach for the Maximum subarray problem: "))

#global variable because python is dumb
dcTimeArray = [0] * arrayLength

def bruteForce(numArray, low, high):
    maxProfit = 0
    maxLeft = None
    maxRight = None
    i = low
    while i <= high:
        j = i + 1
        while j < high:
            profit = numArray[j] - numArray[i]
            if (profit > maxProfit):
                maxLeft = i 
                maxRight = j
            j = j + 1
        i = i + 1

def dcAlgorithm3(numArray, low, high):
    if high == low:
        return(low, high, numArray[low])
    else:
        mid = math.floor((low + high)/2)
        leftStart, leftEnd, leftMax = dcAlgorithm3(numArray, low, mid)
        rightStart, rightEnd, rightMax = dcAlgorithm3(numArray, mid + 1, high)
        crossStart, crossEnd, crossMax = dcCrossingAlgorithm3(numArray, low, mid, high)
        if (leftMax > rightMax and leftMax > crossMax):
            return leftStart, leftEnd, leftMax
        elif (rightMax > leftMax and rightMax > crossMax):
            return rightStart, rightEnd, rightMax
        else:
            return crossStart, crossEnd, crossMax

def dcCrossingAlgorithm3(numArray, low, mid, high):
    leftSum = -1000000000
    sum = 0
    crossStart = mid
    for i in range(mid - 1, low - 1, -1):
        sum = sum + numArray[i]
        if sum > leftSum:
            leftSum = sum
            crossStart = i
    rightSum = -1000000000
    sum = 0
    crossEnd = mid + 1
    for i in range(mid, high):
        sum = sum + numArray[i]
        if sum > rightSum:
            rightSum = sum
            crossEnd = i + 1
    return crossStart, crossEnd, leftSum + rightSum

def dcHelper(numArray, low, high): 
    if high == arrayLength - 1:
        #print("iteration (last)", high)
        start = time.time()
        startt, endd, max = dcAlgorithm3(numArray, low, high)
        end = time.time()
        dcTimeArray[high] = ((end - start) * 1000)
    else:    
        #print("iteration ", high)
        start1 = time.time()
        startt, endd, max = dcAlgorithm3(numArray, low, high)
        end1 = time.time()
        dcTimeArray[high] = ((end1 - start1) * 1000)
        dcHelper(numArray, 0, high + 1)


if methodChoice == 'A':
    save = input('Would you like to save the plot? (Y/N): ')
    print('Close the pop-up window to quit the program.\n')
    x = 0
    array = [randrange(-1000,1000) for arrayLength in range(arrayLength)]
    nArray = [0] * arrayLength
    timeArray = [0] * arrayLength
    nArray = range(0, arrayLength)
    fig, ax = plt.subplots()
    while x < arrayLength:
        y = 0
        tempArray = [0] * (x + 1)
        while y <= x:
            tempArray[y] = array[y]
            y = y + 1
        #---------------------------
        start = time.time()
        bruteForce(tempArray, 0, x)
        end = time.time()
        #---------------------------
        timeArray[x] = (end - start) * 1000
        x = x + 1
    ax.plot(nArray, timeArray)
    ax.set_xlabel('n')
    ax.set_ylabel('T (ms)')
    ax.set_title("Brute Force")
    ax.autoscale()
    if save == 'Y':
        fig.savefig("BruteForce.png")
        plt.show()
    else:
        plt.show()

elif methodChoice == 'B':
    save = input('Would you like to save the plot? (Y/N): ')
    print('Close the pop-up window to quit the program.\n')
    array = [randrange(-1000, 1000) for arrayLength in range(arrayLength)]
    nArray = [0] * arrayLength
    timeArray = [0] * arrayLength
    nArray = range(0, arrayLength)
    fig, ax = plt.subplots()
    
    #---------------------------
    dcHelper(array, 0, 0)
    #print(dcTimeArray)
    #---------------------------
    
    ax.plot(nArray, dcTimeArray)
    ax.set_xlabel('n')
    ax.set_ylabel('T (ms)')
    ax.set_title("Recursive Algorithm")
    ax.autoscale()
    if save == 'Y':
        fig.savefig("RecursiveAlgorithm.png")
        plt.show()
    else:
        plt.show()

elif methodChoice == 'C':
    save = input('Would you like to save the plot? (Y/N): ')
    print('Close the pop-up window to quit the program.\n')
    x = 0
    array = [randrange(-1000,1000) for arrayLength in range(arrayLength)]
    nArray = [0] * arrayLength
    bTimeArray = [0] * arrayLength
    nArray = range(0, arrayLength)
    fig, ax = plt.subplots()
    while x < arrayLength:
        y = 0
        tempArray = [0] * (x + 1)
        while y <= x:
            tempArray[y] = array[y]
            y = y + 1
        #---------------------------
        start = time.time()
        bruteForce(tempArray, 0, x)
        end = time.time()
        #---------------------------
        bTimeArray[x] = (end - start) * 1000
        x = x + 1
    #---------------------------
    dcHelper(array, 0, 0)
    #---------------------------
    ax.plot(nArray, bTimeArray, label = 'Brute Force')
    ax.plot(nArray, dcTimeArray, label = 'Recursive Algorithm')
    ax.set_xlabel('n')
    ax.set_ylabel('T (ms)')
    ax.set_title("Brute Force vs. Recursive Algorithm")
    ax.autoscale()
    ax.legend()
    if save == 'Y':
        fig.savefig("BruteVsRecursion.png")
        plt.show()
    else:
        plt.show()

else:
    print("That is not a choice. Please run the program again.")