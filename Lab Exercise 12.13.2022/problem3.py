## Lab Exercise 12/13/2022 Problem 3
## Author:
## This program will test Goldbach's Conjecture
from math import sqrt

def isPrime(n):
    #Add code here
    

def makePrimeList(num):
    #Add code here
    
            
def goldbach(num, pl):
    #Add code here

    

#test code
found = False
#Test all even numbers to 10000
#Do not test the number 2
for number in range(4, 1000, 2):
    #Create a prime list for the number you are testing
    pl = makePrimeList(number)

    #pass the number you are testing and the prime list to
    #goldbach funtion
    temp = goldbach(number, pl)

    #if you get back an empty list, you found a number that
    #disproves Goldbach's Conjecture
    if len(temp)==  0:
        foundNumber = number
        found = True
        break;

if not found:
    print("You have verified Goldbach's Conjecture for numbers to 1000")
else:
    print("You have disproven Goldbach's Conjecture for", foundNumber)


        
