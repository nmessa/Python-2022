#Using itertools to find permuations of letters
#Author: nmessa
#Date: 12/6/2022

from itertools import permutations

#Get list of letters
word = input("Enter a list of letters: ").lower()

perms = []
#find i-letter words
for i in range(2, len(word)+ 1):
  p = list(permutations(word, i))
  perms += p #Add i-letter words to permutation list
 
  # Print the obtained permutations
for j in perms:
  print(''.join(j))
print (len(perms))
