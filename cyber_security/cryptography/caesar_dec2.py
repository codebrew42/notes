def caesar_decrypt(text, shift_val):
	output = [] #init
	for char in text:
		if char.isalpha():
			if char.isupper():
				start = ord('A')
			else:
				start = ord('a')
			output.append(chr(start + (ord(char) - start + shift_val) % 26))
		else:
			output.append(char)
	#print(output)
	return ''.join(output)

input = "wpjvJAM{jhlzhy_k3jy9wa3k_86kl32k2}%"
decoded = caesar_decrypt(input, -7)
print("decoded: ", decoded)