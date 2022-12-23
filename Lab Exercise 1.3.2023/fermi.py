## Game of Fermi Version 0.5
## Author: 
## Date: 1/3/2023
## The goal of the game is for the player to guess the digits in
## the three positions in the least number of tries.  For each guess,
## the player provides three digits for position 1, 2, and 3.
## The program replies with a hint consisting of Fermi, Pico, and Nano.
## If the digit guess for a given position is correct, then the reply is Fermi.
## If the digit guessed for a given position is in a different position, then
## the reply is Pico.  If the digit guessed for a given position does not match
## any of the three digits, then the reply is Nano.  

from random import *

numbers = [1,2,3,4,5,6,7,8,9]
again = True

while again:
    #Build the secret number of 3 unique numbers from 1 to 9
    #Create a empty list named secret
    #Add code here

    #Fill list with 3 unique numbers
    #Add code here


    #Initialize variables
    win = False
    numGuesses = 0  #keep track of numbers guessed

    #Play a round
    while not win:
        #initialize counter and phrase list
        count = 0
        phrases = []

        #Get number guess from user and split to 3 values
        #Add code here


        #Build a list that represents the number guessed
        #Add code here


        #update number of guesses
        #Add code here


        #Algorithm to test number and generate 3 phrases
        #Add code here


        #Print the result of algorithm execution
        for p in phrases:
            print(p, end = ' ')
        print()
        
        if phrases.count('Fermi') == 3:  #this means you won
            print('You won in', numGuesses, 'guesses')
            win = True

    answer = input("Play again (y/n)? ")
    if answer == 'n':
        again = False

## Sample Output
## Enter 3 numbers (1 - 9): 6 3 5
## Nano Pico Nano 
## Enter 3 numbers (1 - 9): 3 4 2
## Pico Pico Nano 
## Enter 3 numbers (1 - 9): 4 3 7
## Fermi Pico Nano 
## Enter 3 numbers (1 - 9): 4 8 3
## Fermi Fermi Fermi 
## You won in 4 guesses
