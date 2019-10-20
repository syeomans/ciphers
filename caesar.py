alphabet = list("abcdefghijklmnopqrstuvwxyz")

def caesar(inputString, mode, numShifts):
	"""Substitution cipher that shifts the alphabet by some number of spaces.

	Example:
		Plaintext:	We are routed, fall back!
		Shifts:		1
		Ciphertext: Xf bsf spvufe, gbmm cbdl!

	Args:
		inputString (str): plaintext if encrypting or ciphertext if decrypting
		mode (str): 'e' for encryption or 'd' for decryption
		numShifts (str): the number of times to shift the alphabet

	Returns:
		str: plaintext if [mode] is 'd' or ciphertext if [mode] is 'e'
	"""

	# Sanitize inputs
	if mode not in ['e', 'd']:
		raise Exception("'mode' must be either 'e' for encryption or 'd' for decryption")

	# Initialize local variables
	outString = ""

	# Iterate on each character of the input string.
	for inputChar in inputString:

		# If this character is in the alphabet, encode it
		if inputChar.lower() in alphabet:
			# Find starting position of the input character
			startPosition = alphabet.index(inputChar.lower())
			# Encode or decode the input character by shifting the alphabet
			if mode == 'e': # encode
				outputChar = alphabet[(startPosition + numShifts) % len(alphabet)]
			elif mode == 'd': # decode
				outputChar = alphabet[(startPosition - numShifts) % len(alphabet)]
			# Preserve capitalization
			if inputChar.isupper():
				outputChar = outputChar.upper()

		# If character is not in alphabet, preserve punctutation
		else:
			outputChar = inputChar

		# Append to output string
		outString += outputChar

	# Write to file
	return(outString)
