## Lab Exercise 12/13/2022 Problem 1
## Author: 
## This program will calculate your weight on other planets.

#create a dictionary (planets) that maps the planet name to conversion factor
planets = {'Mercury':0.4155, 'Venus':0.8975, 'Earth':1.0, 'Moon':0.166,
           'Mars':0.3507, 'Jupiter':2.5374, 'Saturn':1.0677,
           'Uranus':0.8947, 'Neptune':1.1794, 'Pluto':0.0899,
           'Eric Clapton':5.78e-10, 'Jerry Garcia':1.95e-9}

#Create a dictionary (menuToPlanet) that maps choice to [;amet name
menuToPlanet = {1:'Mercury', 2:'Venus', 3:'Earth', 4:'Moon', 5:'Mars',
              6:'Jupiter', 7:'Saturn', 8:'Uranus', 9:'Neptune',
                10:'Pluto', 11:'Eric Clapton', 12:'Jerry Garcia'}

def displayMenu():
    #Add code here
    

def findWeight(weight, planet):
    #Add code here
    

choice = displayMenu()
myWeight = float(input("How much do you weigh? "))
planetWeight = findWeight(myWeight, menuToPlanet[choice])
print ("You weigh", planetWeight, 'pounds on', menuToPlanet[choice])
    
