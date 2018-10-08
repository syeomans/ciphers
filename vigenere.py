alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encode(plaintext, key):
	# Make message and key uppercase
	plaintext = plaintext.upper()
	key = key.upper()

	# Repeat key until its length matches the length of the message. Preserve whitespace.
	keystream = ""
	i = 0
	for letter in plaintext:
		# Preserve whitespace and punctuation
		if letter  not in alphabet:
			keystream += letter
		else:
			keystream += key[i % len(key)]
			# Only increment counter in this case
			i += 1

	# Encode message 
	ciphertext = ""
	i = 0
	for letter in plaintext:
		# Preserve whitespace and punctuation
		if letter  not in alphabet:
			ciphertext += letter
		# Offset this letter based on the keystream
		else:
			alphabetPosition = alphabet.index(letter)
			offset = alphabet.index(keystream[i])
			ciphertext += alphabet[alphabetPosition + offset]
		# In either case, increment counter
		i += 1
	return(ciphertext)

def decode(ciphertext, key):
	# Make key uppercase
	key = key.upper()

	# Repeat key until its length matches the length of the message. Preserve whitespace.
	keystream = ""
	i = 0
	for letter in ciphertext:
		# Preserve whitespace and punctuation
		if letter  not in alphabet:
			keystream += letter
		else:
			keystream += key[i % len(key)]
			# Only increment counter in this case
			i += 1

	# Decode message 
	plaintext = ""
	i = 0
	for letter in ciphertext:
		# Preserve whitespace and punctuation
		if letter  not in alphabet:
			plaintext += letter
		# Offset this letter based on the keystream
		else:
			alphabetPosition = alphabet.index(letter)
			offset = alphabet.index(keystream[i])
			plaintext += alphabet[alphabetPosition - offset]
		# In either case, increment counter
		i += 1
	return(plaintext)

