##Lab Exercise 1.18.2023 Problem 5
##Author: 

#Define the dictionary
string_maps = {"1":"abc", "2":"def", "3":"ghi", "4":"jkl", "5":"mno", "6":"pqrs",
               "7":"tuv", "8":"wxy", "9":"z"}
#Create an empty list to hold all 2 character permutations
strings = []

#Generate all 2 character permutations
for key in string_maps.keys():
    #Add code here


    

#Print the permutation list
for i in range(len(strings)):
    print(strings[i], end = ' ')
    if i % 12 == 0 and i != 0:
        print()
        
##Output
##ab ac ba ca bc cb de df ed fd ef fe gh 
##gi hg ig hi ih jk jl kj lj kl lk mn 
##mo nm om no on pq pr ps qp qr qs rp 
##rq rs sp sq sr tu tv ut vt uv vu wx 
##wy xw yw xy yx 
