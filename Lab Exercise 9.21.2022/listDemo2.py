#List Demo 2
#Author: nmessa
#Date: 9.15.2007

#define two lists
list1 = [3,6,4,2,1]
list2 = [8,13,7,32,67,14]

#Concatenation
list3 = list1 + list2    #concatenate two lists
print( 'List 3 =', list3)

#Repetition
list4 = list1 * 3   #triple the list
print( 'List 4 =', list4)

#indexing, repetition, and length
print( 'List 2 elements')
for i in range(len(list2)): #print each element of the list
    print (list2[i])

#slicing
print( list4[3:6])   #prints elements 3, 4, and 5

#Membership
print (13 in list2)  #checks to see if 13 is in list2

#append
list1.append(999) #add 999 to end of list
print( list1)

#sorting
list2.sort()  #sort the list
print (list2)

#reverse
list2.reverse()  #reverse the list
print (list2)

#count
print( list4)
print (list4.count(6))  #count the number of 6's in the list

#pop
print (list2)
list2.pop(0)  #remove element 0 from the list
print( list2)

#insert
print (list2)
list2.insert(2, 777) #insert 777 at position 2
print (list2)

#Output
##List 3 = [3, 6, 4, 2, 1, 8, 13, 7, 32, 67, 14]
##List 4 = [3, 6, 4, 2, 1, 3, 6, 4, 2, 1, 3, 6, 4, 2, 1]
##List 2 elements
##8
##13
##7
##32
##67
##14
##[2, 1, 3]
##True
##[3, 6, 4, 2, 1, 999]
##[7, 8, 13, 14, 32, 67]
##[67, 32, 14, 13, 8, 7]
##[3, 6, 4, 2, 1, 3, 6, 4, 2, 1, 3, 6, 4, 2, 1]
##3
##[67, 32, 14, 13, 8, 7]
##[32, 14, 13, 8, 7]
##[32, 14, 13, 8, 7]
##[32, 14, 777, 13, 8, 7]
