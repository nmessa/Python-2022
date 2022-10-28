# zeller.py
# Author: nmessa
# Lab Exercise 11.04.2014 Problem 4
# This is some starter code where I have defined 3 dictionaries for converting month numbers,
# month names, and day names.  I have also provided the code for getting user input, processing user
# input, and printing the processed result.  You should read through this code and attempt to understand
# it before blindly using it.

#conversion dictionaries
monthNumber = {'01':11, '02':12, '03':1, '04':2, '05':3, '06':4, '07':5, '08':6, '09':7, '10':8, '11':9, '12':10}
monthName = {'01':'January', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June', '07':'July', \
             '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'}
dayName = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}

#Get input from user
temp =raw_input("Enter the date in the format mm/dd/yyyy: ")

#Process the string to give month, day and year as integers
myDate = temp.split('/')
month = monthNumber[myDate[0]]
day = int(myDate[1])
year = int(myDate[2])

#Make calculations
#ADD YOUR CODE HERE







#Print the output
dayOfWeek = dayName[R]
print monthName[myDate[0]], myDate[1], ', ', myDate[2], 'falls on', dayOfWeek
