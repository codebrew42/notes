def caesar_shift(text, shift_val):
	output = []		#init an empty list to store

	#iterate over the parameter which is given on the terminal
	for char in text:
		if char.isalpha():
			if char.isupper():
				start = ord('A')		#get unicode point for ()
			else:
				start = ord('a')
			shifted = chr(start + (ord(char) - start + shift_val) % 26) #chr(): unicode->char
			output.append(shifted)
		else:
			output.append(char)
	return ''.join(output)

input = "wpjvJAM{jhlzhy_k3jy9wa3k_86kl32k2}%"
decoded = caesar_shift(input, -7)
print("decoded: ", decoded)

##note
# ord('A') = 65
# ord('B') = 66
# shift by 3
# or(ord('A') + (ord('B') - ord('A') + 3) % 26)
# 66 - 65 + 3 ord('E') % 26 = ord('E')