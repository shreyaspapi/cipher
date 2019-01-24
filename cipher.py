import string
import sys
import os

def keyString(key, stringtoencrypt):
    stringMade = ""
    spaces = 0
    for num in range(len(stringtoencrypt)):
        if stringtoencrypt[num] == " ":
            stringMade += " "
            spaces += 1
        else:
            stringMade += key[((num + 1 - spaces) % len(key)) - 1]
    return stringMade

def encrypt(key, toEncrypt):
    alphabets = list(string.ascii_uppercase)
    encryptedString = ""
    strings = toEncrypt.upper()
    keyUsed = keyString(key, strings).upper()

    for num in range(len(toEncrypt)):
        if strings[num] == " ":
            encryptedString += " "
        else:
            encryptedString += alphabets[(((alphabets.index(strings[num])) + (alphabets.index(keyUsed[num]) + 1)) % 26) - 1]
    return encryptedString

def timesToEncrypt(num, key, stringToEncrypt):
    while num: 
        stringToEncrypt = encrypt(key, stringToEncrypt)
        num -= 1
    return stringToEncrypt


key = input("Key of your encryption: ")
stringToEncrypt = input("Input the characters you want to encrypt: ")
timestoencrypt = int(input("No. of times you want to repeat it: "))
print(timesToEncrypt(timestoencrypt, key, stringToEncrypt))
