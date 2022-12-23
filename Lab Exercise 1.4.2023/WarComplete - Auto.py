##Lab Exercise 1.4.2023 Problem 3
##Author: 

# War.py
import random
#define suits
suits = ['clubs', 'diamonds', 'hearts', 'spades']

#define face values
faces = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
         'ten', 'jack', 'queen', 'king', 'ace']

#Create an empty list to hold generated cards
cards = []

#Build deck of cards
#Add code here

        
#Shuffle the deck
#Add code here

#Create and initialize variables
keepGoing = True
hands = 0
ties = 0
my_score = 0
your_score = 0
card_count = 0

#Start game loop
while keepGoing and (hands < 26):
    #add one to hands
    #Add code here
    
    #Get my_card from deck
    #Add code here
    
    #increment card_count
    #Add code here
    
    #Get your_card from desk
    #Add code here
    
    #Increment card_count
    #Add code here

    #Print each player's hand
    #Add code here

    #Print each player's hand
    print ("I have the", my_card)
    print ("You have the", your_card)

    #get face value for each card
    #Add code here


    #Test to see who won
    if faces.index(mc) > faces.index(yc):
        #Add code here
        
    elif faces.index(yc) > faces.index(mc):
        #Add code here
        
    else:
        #Add code here

    #Print current score
    print ("Score: Computer",my_score, ", You",your_score)


#Print results of game
print("Game Over")
if my_score > your_score:
    print ("I win the game!")
elif your_score > my_score:
    print ("You win the game!")
else:
    print ("It was a tie game!")

##Sample Output
##I have the five of clubs
##You have the two of clubs
##I win!
##Score: Computer 1 , You 0
##I have the five of diamonds
##You have the four of clubs
##I win!
##Score: Computer 2 , You 0
##I have the two of spades
##You have the three of spades
##You win!
##Score: Computer 2 , You 1
##I have the seven of spades
##You have the ten of clubs
##You win!
##Score: Computer 2 , You 2
##I have the queen of diamonds
##You have the two of diamonds
##I win!
##Score: Computer 3 , You 2
##I have the ten of spades
##You have the seven of clubs
##I win!
##Score: Computer 4 , You 2
##I have the jack of spades
##You have the two of hearts
##I win!
##Score: Computer 5 , You 2
##I have the ace of hearts
##You have the six of hearts
##I win!
##Score: Computer 6 , You 2
##I have the queen of hearts
##You have the queen of spades
##It's a tie!
##Score: Computer 6 , You 2
##I have the king of spades
##You have the jack of diamonds
##I win!
##Score: Computer 8 , You 2
##I have the five of spades
##You have the seven of diamonds
##You win!
##Score: Computer 8 , You 3
##I have the three of hearts
##You have the ace of clubs
##You win!
##Score: Computer 8 , You 4
##I have the ten of hearts
##You have the ace of diamonds
##You win!
##Score: Computer 8 , You 5
##I have the three of diamonds
##You have the five of hearts
##You win!
##Score: Computer 8 , You 6
##I have the nine of hearts
##You have the eight of clubs
##I win!
##Score: Computer 9 , You 6
##I have the four of diamonds
##You have the seven of hearts
##You win!
##Score: Computer 9 , You 7
##I have the queen of clubs
##You have the king of clubs
##You win!
##Score: Computer 9 , You 8
##I have the four of spades
##You have the jack of clubs
##You win!
##Score: Computer 9 , You 9
##I have the king of diamonds
##You have the three of clubs
##I win!
##Score: Computer 10 , You 9
##I have the ace of spades
##You have the nine of clubs
##I win!
##Score: Computer 11 , You 9
##I have the eight of hearts
##You have the six of spades
##I win!
##Score: Computer 12 , You 9
##I have the ten of diamonds
##You have the four of hearts
##I win!
##Score: Computer 13 , You 9
##I have the eight of diamonds
##You have the six of diamonds
##I win!
##Score: Computer 14 , You 9
##I have the king of hearts
##You have the jack of hearts
##I win!
##Score: Computer 15 , You 9
##I have the nine of diamonds
##You have the six of clubs
##I win!
##Score: Computer 16 , You 9
##I have the eight of spades
##You have the nine of spades
##You win!
##Score: Computer 16 , You 10
##Game Over
##I win the game!
