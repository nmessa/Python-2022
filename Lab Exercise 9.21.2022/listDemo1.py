#List Demo 1
#Author: nmessa
#Date: 9.15.2007


import random

def maxInList(numbers):
    return max(numbers)

def sortList(numbers):
    numbers.sort()

#Declare a list
numbers = [ ]

#Fill the list with a ten random integers
for i in range(10):
    rNumber = random.randint(1, 1000)
    numbers.append(rNumber)

#Get the maximum element in the list
maximum = maxInList(numbers)
print ("maximum value in the list = " + str(maximum))

#Print the original list
print ("The original list: ")
print (numbers)
print()
sortList(numbers)
#Print the sorted list
print ("The sorted list:")
print (numbers)   

#Output
##maximum value in the list = 930
##The original list: 
##[305, 796, 457, 930, 925, 42, 401, 402, 35, 262]
##
##The sorted list:
##[35, 42, 262, 305, 401, 402, 457, 796, 925, 930]
