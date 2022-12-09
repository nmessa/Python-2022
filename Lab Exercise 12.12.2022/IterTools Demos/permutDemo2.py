#Using itertools to find permuations of letters
#Author: nmessa
#Date: 12/6/2022

from itertools import permutations

#read in words from word file
inFile = open('words.txt', 'r')
wordList = []
for line in inFile:
  wordList.append(line.strip().lower())
print ("  ", len(wordList), "words loaded.")

#Get list of letters
word = input("Enter a list of letters: ").lower()

#Create lists to hold permutations, words, and real words
perms = []
words = []
realWords = []

#find i-letter permutations
for i in range(2, len(word)+ 1):
  p = list(permutations(word, i))
  perms += p #Add i-letter words to permutation list
 
# convert permutations to words
for j in perms:
  words.append(''.join(j))

#make a list of real words
for w in words:
  if w in wordList:
    realWords.append(w)

#print real words   
for r in realWords:
  print(r)


