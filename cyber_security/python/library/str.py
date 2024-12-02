import string


def b16_encode(c):
	print("0:08: {0:08b} ".format(ord(c)), end='') 
	print("0:20: {0:20b} ".format(ord(c)), end='') 
	print("0:05: {0:05b} ".format(ord(c)), end='') # try to truncate the leftmost bits up to 5 bits
	print()

print("(c) ", b16_encode('c'))

print("(A) ", b16_encode('A'))

print("(!) ", b16_encode('!'))

