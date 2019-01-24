import string

def encrypt(key, toEncrypt):
    alphabets = list(string.ascii_uppercase)
    encryptedString = ""
    string = toEncrypt.upper()
    keyString = key*(len(toEncrypt)/len(key))

    for num in range(len(toEncrypt)):
        encryptedString += alphabets[(((alphabets.index(toEncrypt[num]) + 1) + (alphabets.index(keyString[num]) + 1)) % 26) - 1]
    return encryptedString

def timesToEncrypt(num, key, stringToEncrypt):
    while num: stringToEncrypt = encrypt(key, stringToEncrypt)
        num -= 1
    return stringToEncrypt

if __name__ == "__main__":

