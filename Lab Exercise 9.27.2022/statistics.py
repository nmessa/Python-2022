#Statistics module
#Author: nmessa
#Date: 10.13.2020

def calcMean(numbers):
    mean = sum(numbers)/len(numbers)
    return mean

def findMedian(numbers):
    numbers.sort()
    middle = len(numbers)//2
    if len(numbers) % 2 == 0:
        median = (numbers[middle] + numbers[middle - 1])/2
    else:
        median = numbers[middle]
    return median

def findLargest(numbers):
    numbers.sort()
    maxValue = numbers[-1]
    return maxValue

def findSmallest(numbers):
    numbers.sort()
    minValue = numbers[0]
    return minValue

def findRange(numbers):
    return findLargest(numbers) - findSmallest(numbers)
