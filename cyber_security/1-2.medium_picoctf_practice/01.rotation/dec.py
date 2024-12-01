def dec(input, shift_val):
	output = []
	for char in input:
		if char.isalpha():
			if char.isupper():
				start = ord('A')
			else:
				start = ord('a')
			output.append(chr(start + (ord(char) - start + shift_val) % 26))
		else:
			output.append(char)
	return ''.join(output)


input = "xqkwKBN{z0bib1wv_l3kzgxb3l_949in1i1}"
output = dec(input, -8)
print("decoded: ", output)