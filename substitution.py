import random
import string

def randAlphabet(alphabet=string.ascii_lowercase):
    """Create a random alphabet

    Args:
        alphabet (str): the original, in-order alphabet to use
            (default: latin alphabet with no numbers)

    Returns:
        str: a scrambled alphabet
    """

    # Make a copy of the alphabet and scramble it
    cipherAlphabet = list(alphabet.lower())
    random.shuffle(cipherAlphabet)
    # Turn into a string
    returnValue = "".join(cipherAlphabet)
    return(returnValue)

def substitution(inputString, mode, cipherAlphabet, plainAlphabet=string.ascii_lowercase):
    """Encode a message with a substitution cipher

    Substitution ciphers use a cipher alphabet to map plaintext to ciphertext.

    Example:
        Plaintext alphabet:	    ABCDEFGHIJKLMNOPQRSTUVWXYZ
        Ciphertext alphabet:	ZEBRASCDFGHIJKLMNOPQTUVWXY
        Message:                FLEE AT ONCE. WE ARE DISCOVERED!
        Ciphertext:             SIAA ZQ LKBA. VA ZOA RFPBLUAOAR!

    This implementation preserves capitalization and punctuation. Some pre-
    processing may be necessary if you want to exclude these.

    Numbers can be mapped by including them in the cipher- and plaintext-
    alphabets. For example,
        plainAlphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        cipherAlphabet = "mnbvcxzlkjhgfdsapoiuytrewq0987654321"

    Keep in mind if one side of each alphabet is all numbers and the other is
    all characters, the cipher will always substitute numbers with numbers and
    characters with characters. To add more cryptographic confusion, you may
    want to mix numbers and characters throughout the cipher alphabet.
        ex: "i0ujncy5bsvq9e8o2gflmk461xtapd7w3hzr"

    Args:
        inputString (str): plaintext if encrypting or ciphertext if decrypting
		mode (str): 'e' for encryption or 'd' for decryption
		cipherAlphabet (str): the new, in-order alphabet to map to
            ex: "mnbvcxzlkjhgfdsapoiuytrewq"
        plainAlphabet (str): the original, in-order alphabet (optional)
            ex: "abcdefghijklmnopqrstuvwxyz"

    Returns:
        str: plaintext if [mode] is 'd' or ciphertext if [mode] is 'e'
    """

    # Sanitize inputs
    cipherAlphabet = cipherAlphabet.lower()
    if mode not in ['e', 'd']:
        raise Exception("'mode' must be either 'e' for encryption or 'd' for decryption")

    # Initialize local varaibles
    outputString = ""

    # Swap the characters of the input string with the cipher alphabet
    for inputChar in inputString:
        if inputChar.lower() in plainAlphabet:
            # Encode or decode this character
            if mode == 'e': # encode
                newPosition = plainAlphabet.index(inputChar.lower())
                outputChar = cipherAlphabet[newPosition]
            elif mode == 'd': # decode
                newPosition = cipherAlphabet.index(inputChar.lower())
                outputChar = plainAlphabet[newPosition]

            # Make capital if the input is capital (bad cryptography, but fun)
            if inputChar.isupper():
                outputChar = outputChar.upper()

        # Preserve punctuation
        else:
            outputChar = inputChar

        # Append to output string
        outputString += outputChar

    return(outputString)
