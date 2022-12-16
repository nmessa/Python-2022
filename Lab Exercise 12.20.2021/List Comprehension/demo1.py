#Demo 1
## Author: nmessa
## Date 12.15.2015

# Create a list of words
words = 'The quick brown fox jumps over the lazy dog'.split()
print (words)
print()
print()

# Create a list of the words in upper case, lower case and their length
# using list comprehension
stuff = [[w.upper(), w.lower(), len(w)] for w in words]

for i in stuff:
    print (i)

## Output
## ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
##
##
## ['THE', 'the', 3]
## ['QUICK', 'quick', 5]
## ['BROWN', 'brown', 5]
## ['FOX', 'fox', 3]
## ['JUMPS', 'jumps', 5]
## ['OVER', 'over', 4]
## ['THE', 'the', 3]
## ['LAZY', 'lazy', 4]
## ['DOG', 'dog', 3]
