# Implementation of Caesar Cipher, both small and capital letters allowed

def generate_cipher(string, shift):

    encrypted = ''
    for letter in string:
        if letter.isupper():
            encrypted += chr((ord(letter) + shift - 65) % 26 + 65)
            # lower case characters
        else:
            encrypted += chr((ord(letter) + shift - 97) % 26 + 97)

    return encrypted


cipher, shift = input().split(' ')
print(generate_cipher(cipher, int(shift)))




