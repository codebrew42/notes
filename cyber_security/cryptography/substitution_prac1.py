
def	substitute(input):
	output = []
	arr1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	arr2 = "OHNFUMWSVZLXEGCPTAJDYIRKQB"
	arr3 = "ohnfumwsvzlxegcptajdyirkqb"
	for char in input:
		if char.isalpha():
			if char.isupper():
				output.append(arr1[arr2.index(char)])
			else:
				output.append(arr1[arr3.index(char)].lower())
		else:
			output.append(char)
	return ''.join(output)

input = "Dsu mxow vj: pvncNDM{5YH5717Y710G_3I0XY710G_03055505}"
output = substitute(input)
print("decoded: ", output)