from functools import reduce
from random import randrange

def factors(n):
    # Courtesy of https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    return list(reduce(list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def generateKeys(p, q):
        '''
        Given two prime numbers p and q, generate a pair of public
        and private keys using the RSA algorithm.

        Returns a JSON-like object containing public and private keys.
        '''
        # n is the modulus for the public key and the private keys
        n = p*q

        # phi(n) is the totient; the number of coprimes between p and q
        phi = (p-1)*(q-1)

        # Select encryption key e such that e and
        # (p - 1)(q - 1) have only 1 as a factor in common.
        # (choose the smallest number for speed; this is for educational purposes only)
        badValues = factors(phi) # List of values e can't be
        badValues.append(p) # e also has to be coprime with n, which only has 2 factors: p and q
        badValues.append(q)
        e = 1 # Start with a bad value so we can start the loop
        while e in badValues: # Choose a random integer between 1 and phi(n) until e is a good value
            # e = randrange(phi) # Do this for security
            e += 1 # Do this for speed

        # Find a value for d such that d is the multiplicative inverse of e in
        # modular arithmetic. i.e, find d such that (d*e) % phi(n) = 1
        # (choose the smallest number for speed; this is for educational purposes only)
        d = 1
        while d*e%phi != 1:
            d += 1

        # Return a JSON-like object containing public and private keys
        return({'publicKey':{'n':n, 'd':d}, 'privateKey':{'n':n, 'e':e}})

def encrypt(plaintext, e, n):
    asciiPlaintext = []
    asciiCiphertext = []

    # Convert plaintext to list of ascii values (for simplicity)
    for character in plaintext:
        asciiPlaintext.append(ord(character))

    # Encryption formula: ci = mi^e mod n
    for character in asciiPlaintext:
        asciiCiphertext.append(character**e % n)

    return(asciiCiphertext)

def decrypt(asciiCiphertext, d, n):
    asciiPlaintext = []
    plaintext = ''

    # Decryption formula: mi = ci^d mod n
    for character in asciiCiphertext:
        asciiPlaintext.append(character**d % n)

    # Convert plaintext ascii characters to ciphertext
    for character in asciiPlaintext:
        plaintext += chr(character)

    return(plaintext)


# # Test script
# myKeys = generateKeys(11, 17)
# print(myKeys)
#
# n = myKeys['privateKey']['n']
# e = myKeys['privateKey']['e']
# message = "Hello, world!"
# ciphertext = encrypt(message, e, n)
# print(ciphertext)
#
# d = myKeys['publicKey']['d']
# plaintext = decrypt(ciphertext, d, n)
# print(plaintext)
