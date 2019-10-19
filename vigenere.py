alphabet = list("abcdefghijklmnopqrstuvwxyz")

def vigenere(inputString, mode, key, preserveCaps=True, preservePunctuation=True):
	"""Encrypt a message using a Vigenere cipher

	The Vigenere cipher is a polyalphabetic substitution cipher that shifts
	the alphabet by some amount determined by a key per each  plaintext
	character.

	The Vigenere cipher iterates over each character in the plaintext together
	with each character in the key (repeating the key as necessary).
	At each step, the cipher shifts the alphabet until the first letter of the
	cipher alphabet starts with this letter of the key. Essentially, the
	cipher uses a different Cesar cipher for each plaintext character and uses
	the key to determine which Cesar cipher to map to. Traditionally, a
	Vigenere table was used to encode this by hand (see below).

	Abridged Vigenere table:
	key character	| 	cipher alphabet
	a 				| 	abc...xyz
	b 				| 	bcd...yza
	c 				| 	cde...zab
	...				| 	...
	z 				| 	zab...wxy

	Example:
		Plaintext:	ATTACKATDAWN
		Key:		LEMON
		Ciphertext:	LXFOPVEFRNHR

	Args:
		inputString (str): plaintext if encrypting or ciphertext if decrypting
		mode (str): 'e' for encryption or 'd' for decryption
		key (str): a password of sorts used to encrypt the message
		preserveCaps (bool): flag to preserve capitalization (default: True)
		preservePunctuation (bool): flag to preserve non-characters, including
			spaces and numbers (default: True)

	Returns:
		str: plaintext if [mode] is 'd' or ciphertext if [mode] is 'e'
	"""

	# Sanitize inputs
	key = key.lower()
	key.replace(" ", "")
	if mode not in ['e', 'd']:
		raise Exception("'mode' must be either 'e' for encryption or 'd' for decryption")

	# Initialize local variables
	keystreamCounter = 0
	outString = ""

	# Iterate on each character of the input string.
	for inputChar in inputString:
		# If this character is in the alphabet, encode it
		if inputChar.lower() in alphabet:
			# Find the number of positions to move and the starting position
			keyChar = key[keystreamCounter % len(key)]
			numMoves = alphabet.index(keyChar)
			startPosition = alphabet.index(inputChar.lower())

			# Encode or decode the input character by shifting the alphabet
			if mode == 'e': # encode
				outputChar = alphabet[(startPosition + numMoves) % len(alphabet)]
			elif mode == 'd': # decode
				outputChar = alphabet[(startPosition - numMoves) % len(alphabet)]

			# Preserve capitalization if specified
			if inputChar.isupper() & preserveCaps:
				outputChar = outputChar.upper()

			# Increment counter on each loop.
			keystreamCounter += 1

		# If character is not in alphabet, preserve punctutation if specified
		elif preservePunctuation:
			outputChar = inputChar

		# Otherwise, do nothing
		else:
			outputChar = ""

		# Append to output string
		outString += outputChar

	# Write to file
	return(outString)
