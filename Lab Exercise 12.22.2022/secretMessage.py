##Lab Exercise 12.22.2022 Problem 3
##Author: 
##This program demonstrates Caesar Cipher using the ASCII value of your name
##as the key

#This function generates a key value based on your name
#This function adds up the ASCII values of all letters in your name
#and returns a value from 13 to 127
def nameValue(name):
    #Add code here

#This function takes plainText and a key and encrypts it using Caesar Cipher
def encrypt(plainText, key):
    #Add code here

#This function takes cipherText and a key and decrypts it using Caesar Cipher
def decrypt (cipherText, key):
    #Add code here


#Test code
plainText = input("Enter a phrase: ")
name = input("Enter your first name: ").lower()
key = nameValue(name)
cipherText = encrypt(plainText, key)
print('Encrypted message =', cipherText)
print()
name = input("Enter your first name to decrypt: ").lower()
key = nameValue(name)
plainText = decrypt(cipherText, key)
print('Original message =', plainText)

## Output
## Enter a phrase: This is my secret message
## Enter your first name: Norman
## Encrypted message = ÈÜÝçÝçáíçÙ×æÙèáÙççÕÛÙ
## Original message = This is my secret message
