'''
Substitution cipher that shifts the alphabet by some number of spaces.
'''

import string
alphabet = list(string.ascii_uppercase)

def encrypt(message, offset=1):

    # Convert text to a list of uppercase characters
    message = list(message.upper())

    # Walk the list and shift each character by the specified offset
    ciphertext = ''
    for i in range(0,len(message)):
        if message[i] in alphabet: # Only change letters
            # Get the position of this character in the alphabet (ex: A=0, B=1...)
            plaintextIndex = alphabet.index(message[i])
            # Shift this index by the offset, wrapping around to 0 if needed
            ciphertextIndex = (plaintextIndex + offset) % 26
            # Put that character in the ciphertext string
            ciphertext += alphabet[ciphertextIndex]
        else: # Don't change punctuation and stuff
            ciphertext += message[i]

    return(ciphertext)

def decrypt(message, offset=1):

    # Convert text to a list of uppercase characters
    message = list(message.upper())

    # Walk the list and shift each character by the specified offset
    plaintext = ''
    for i in range(0,len(message)):
        if message[i] in alphabet: # Only change letters
            # Get the position of this character in the alphabet (ex: A=0, B=1...)
            ciphertextIndex = alphabet.index(message[i])
            # Shift this index by the offset, wrapping around to 0 if needed
            plaintextIndex = (ciphertextIndex - offset + 26) % 26
            # Put that character in the ciphertext string
            plaintext += alphabet[plaintextIndex]
        else: # Don't change punctuation and stuff
            plaintext += message[i]

    return(plaintext)

# # Test script
# message = "Hello, world!"
# offset = 10
# ciphertext = encrypt(message, offset)
# print(ciphertext)
# plaintext = decrypt(ciphertext, offset)
# print(plaintext)
