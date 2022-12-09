## Lab Exercise 12/15/2022
## Author: 
## This implements the Player class
## player.py

from die import Die

class Player():
    def __init__ (self):
        #Add code here

    def getNumberOfRolls(self):
        #Add code here

    def play(self):
        #Add code here
        

    def __str__(self):
            result = ""
            for (d1, d2) in self.rolls:
                result += str((d1, d2)) + "\t" + str(d1 + d2) + '\n'
            return result
#end of player class
