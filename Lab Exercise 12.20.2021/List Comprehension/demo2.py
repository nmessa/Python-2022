## Demo 2
## Author: nmessa
## Date 12.15.2015
## Create a table of numbers


# Create a list of numbers using list comprehension
print ("N\t", "N^2\t", "Sqrt(N)")
stuff = [[num, num**2, num**0.5] for num in range(100)]
for i in stuff:
    #print (i)
    print (i[0], '\t', i[1], '\t', i[2])
