##This program creates a word list of 55900 words
##THe words in this word list are from the Massachusetts Institute of Technology
##Freshman Computer Science 1 course.  Thew words are found in a text file on one line
##and each word is seperated by a space.
##The wordList is then filtered into short, medium, and long word lists
##Short = less that 4 letters
##Medium = 4 to 7 letters inclusive
##Long = greater that 7 letters


##Author: nmessa
##Date: 11/30/2022

#Open the file words.txt for reading
#Add code here

#Read the line and store in a string variable
#Add code here

#Split the line and store in a list named wordList
#Add code here

#Close the file
#Add code here

#Create 3 lists to hold short, medium, and long words
shortWords = []
mediumWords = []
longWords = []

#check each word in the word list and add to the appropriate list
#Add code here


#Output the results
print(len(shortWords), "short words")
print(len(mediumWords), "medium length words")
print(len(longWords), "long words")

##Output
##584 short words
##25581 medium length words
##29735 long words
