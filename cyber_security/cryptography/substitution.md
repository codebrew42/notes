# when a key set is given
- use arr
- use arr.index(char) : and find the first occurance

## code-example
```python3
print("lower 'a': ", ord('a'))
print("lower 'A': ", ord('A'))

def	decode(text):
	output = []
	arr1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	arr2 = "OHNFUMWSVZLXEGCPTAJDYIRKQB"
	arr3 = "ohnfumwsvzlxegcptajdyirkqb"
	for char in text:
		if char.isalpha():
			if char.isupper():
				output.append(arr1[arr2.index(char)])
			else:
				output.append(arr1[arr3.index(char)].lower())
		else:
			output.append(char)
	return ''.join(output)

input = "Dsu mxow vj: pvncNDM{5YH5717Y710G_3I0XY710G_03055505}"
#input = "Suauypcg Xuwaogf oacju, rvds o waoiu ogf jdoduxq ova."
output = decode(input)
print("decoded: ", output)
```