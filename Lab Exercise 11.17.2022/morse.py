# morse.py
# This program will convert a user provided phrase into Morse Code
# and flash an LED with the code
# Author: nmessa
# Date: 10.27.2021

from machine import Pin
import time

def codeGen(s):
    output = ''
    s = s.lower()    #put string in lower case to reduce dictionary size
    for i in range(len(s)):
        if s[i] == '\n':
            output += '\n'
            continue
        output += convert(s[i])
        output += ' '
    print (output)
    for i in range(len(output)):
        if output[i] == '.':
            dot()
        if output[i] == '-':
            dash()
        if output[i] == ' ':
            time.sleep(0.1)

def convert(letter):
#International Morse Code dictionary
    table = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.',
             'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---',
             'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---',
             'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
             'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--',
             'z':'--..', ' ':'       ', '1':'.----', '2':'..---',
             '3':'...--', '4':'....-', '5':'.....', '6':'-....',
             '7':'--...', '8':'---..', '9':'----.', '0':'-----'}
    if letter in table.keys():  #check that letter is in dictionary
        return table[letter]
    else:   #handle other characters where code does not exist in dictionary
        return ''     # 2 single quotes

def dot():
    led.toggle()
    time.sleep(0.1)
    led.toggle()
    time.sleep(0.1)

def dash():
    led.toggle()
    time.sleep(1)
    led.toggle()
    time.sleep(0.1)

#Main program
while True:
    led = Pin(25, Pin.OUT)
    phrase = input("Enter a phrase: ")
    codeGen(phrase)
