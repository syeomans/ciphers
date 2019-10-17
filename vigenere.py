alphabet = list("abcdefghijklmnopqrstuvwxyz")

def vigenere(inputString, mode, key, preserveCaps=True, preservePunctuation=True):
	"""
	The Vigenere cipher is a polyalphabetic substitution cipher that shifts
	the alphabet by some amount determined by a key per each  plaintext
	character.

	The vigenere cipher first expands the key into a keystream to match the
	length of the plaintext. For each pair of plaintext and keystream characters
	(when encoding), the cipher shifts the substitution alphabet by the position
	of the keystream character in the  original alphabet and applies the shifted
	alphabet to the plaintext character.

	Example:
		Plaintext:	ATTACKATDAWN
		Key:		AZTEC
		Keystream:	AZTECAZTECAZ
		Ciphertext:	ASMEEKZMHCWM

	In the above example, the key AZTEC was expanded to be 12 characters long.
	For the first character encoding, the alphabet was shifted by A, which
	evaluates to 0 (or 26 depending on how you look at it) shifts to the right.
	The second character Z shifts by 25 places, the third character T shifts by
	20 places, and so on.

	Key character 	number of shifts
	A 				0
	B 				1
	C 				2
	...
	Z 				25

	Inputs:
		inputString: plaintext if encrypting or ciphertext if decrypting
		mode: 'e' for encryption or 'd' for decryption
		key: a string used to encrypt the message
		preserveCaps: boolean to preserve capitalization (default: True)
		preservePunctuation: boolean to preserve punctuation including spaces
		(default: True)

	Outputs:
		Returns a plaintext string if [mode] is 'd' or a ciphertext string if
		[mode] is 'e'
	"""
	# Sanitize inputs
	key = key.lower()
	key.replace(" ", "")
	if mode not in ['e', 'd']:
		raise Exception("'mode' must be either 'e' for encryption or 'd' for decryption")

	# Initialize variables
	keystreamCounter = -1
	outString = ""

	# Read input string. Iterate on each character. Increment counter at each loop.
	for inputChar in inputString:
		if inputChar.lower() in alphabet:
			keystreamCounter += 1
			# Determine the number of positions to move the plaintext character given the key
			numMoves = alphabet.index(key[keystreamCounter % len(key)])
			# Move the plaintext character
			if mode == 'e':
				outputChar = alphabet[(alphabet.index(inputChar.lower()) + numMoves) % len(alphabet)]
			elif mode == 'd':
				outputChar = alphabet[(alphabet.index(inputChar.lower()) - numMoves) % len(alphabet)]

			# Preserve caps if specified
			if inputChar.isupper() & preserveCaps:
				outputChar = outputChar.upper()

		# Preserve punctutation if specified
		elif preservePunctuation:
			outputChar = inputChar

		# Otherwise, do nothing
		else:
			outputChar = ""

		# Append to output string
		outString += outputChar

	# Write to file
	return(outString)

# Test script
# inputString = open('plaintext.txt', 'r').read()
inputString = "ATTACKATDAWN"
outputString = vigenere(inputString, 'e', 'AZTEC')
print(outputString)
