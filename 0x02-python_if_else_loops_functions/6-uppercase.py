#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if (ord(ch) >96) and (ord(ch) <123): #checks for lowercase
            ch= chr(ord(ch)-32)              #converts lowercasr to uppercase
        print("{}".format(ch), end='')
    print("") 
