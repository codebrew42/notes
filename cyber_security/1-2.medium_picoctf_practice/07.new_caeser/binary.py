import string

binary1 = "{0:08b}".format(ord('c'))
#binary = "{1:08b}".format(ord('c')) #wrong
binary2 = "{0:08b}".format(ord('A'))
binary3 = "{0:08b}".format(ord('!'))
binary4 = "{0:07b}".format(ord('!'))
binary5 = "{0:06b}".format(ord('!'))
binary6 = "{0:05b}".format(ord('!'))

print(binary1)
print(binary2)
print(binary3)
print(binary4)
print(binary5)
print(binary6)

int = 5
formatted1 = "int is {:05}".format(int)

name = "Jin"
formatted2 = "{} is my name".format(name)

print("\n", formatted1)
print(formatted2)
print("-----------------------------------")


to_decode = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"
ALPHA = string.ascii_lowercase[:16]

def decode(to_decode):
	res_to_str = ""
	for i in range(0, len(to_decode), 2):
		if i + 1 >= len(to_decode):
			break
		first = ALPHA.index(to_decode[i])
		second = ALPHA.index(to_decode[i+1])
		res = "{0:04b}{1:04b}".format(first, second)
		res_to_str += chr(int(res, 2))
	return res_to_str

input = "abaa"
result = decode(input)
print(f"{result}")
