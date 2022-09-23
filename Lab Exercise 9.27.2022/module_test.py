## Lab Exercise 9/27/2022 Problems 1 - 5
## Author: nmessa
## This program utilizes my_module to implement a variety of functions

from my_module import *

celsius = float(input("Enter the temperature in degrees C: "))
fahrenheit = c_to_f(celsius)
print (celsius, 'degrees Celsius =', fahrenheit, 'degrees Fahrenheit')

fahrenheit = float(input("Enter the temperature in degrees F: "))
celsius = f_to_c(fahrenheit)
print (fahrenheit, 'degrees Fahrenheit =', celsius, 'degrees Celsius')

five_random()

random_decimals()

## Output
## Enter the temperature in degrees C: 100
## 100 degrees Celsius = 212.0 degrees Fahrenheit
## Enter the temperature in degrees F: 212
## 212 degrees Fahrenheit = 100.0 degrees Celsius
## [19, 19, 7, 16, 17]
## 0.612825595787
## 0.570279323282
## 0.0776831081942
## 0.64004985167
## 0.0840117179737
## 0.979385778261
## 0.192377415519
## 0.497071362458
## 0.670512495327
## 0.152840503389
