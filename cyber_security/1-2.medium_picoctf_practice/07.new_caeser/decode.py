import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
ALPHABET2 = string.ascii_lowercase[:16] + string.ascii_lowercase[:16]
#check
print(f"alphabet2 : {ALPHABET2}")
print("ALPHABET: ", ALPHABET)
print("ALPHABET2: ", ALPHABET2)

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

#check
print(f"LOWERCASE_OFFSET: {LOWERCASE_OFFSET}")
print(f"ord('a'): {ord('a')}")
binary = "{0:08b}".format(ord('a'))
print("binary: ", binary)
print(f"1st int(binary[:4], 2): {int(binary[:4], 2)}")
print(f"2nd int(binary[4:], 2): {int(binary[4:], 2)}")
enc = ""
enc += ALPHABET[int(binary[:4], 2)]
print(f"1st ALPHABET[{int(binary[:4], 2)}] added: {enc}")
enc += ALPHABET[int(binary[4:], 2)]
print(f"2nd ALPHABET[{int(binary[4:], 2)}] added: {enc}")
print("---------------------------------------------------")
print(f"ALPAH[0]: {ALPHABET[0]}")

bin_val = int(format(ord("a"), '08b'), 2)

print(f"bin_val : {bin_val}")
print(f"bin_val * 2 : {bin_val << 4}")

print("---------------------------------------------------")
given_ex = "gb"
i = ALPHABET.index(given_ex[0])
j = ALPHABET.index(given_ex[1])

print(f"idx \"i\": {i}")
print(f"idx \"j\": {j}")
print(f"idx \"j * 16 + j\": {i * 16 + j}")

print(f"idx \"chr(i * 16 + j)\": {chr(i * 16 + j)}")

print("---------------------------------------------------")

def shift(c, k):
	c_idx = ord(c) - LOWERCASE_OFFSET
	k_idx = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(c_idx + k_idx) % len(ALPHABET)] #len(ALPHABET) = 16

flag = "aaa"
key = "a"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

#how it's encoded:
# encoded_str = b16_encode(flag)
# enc = ""
# for i, c in enumerate(encoded_str):
# 	enc += shift(c, key[i % len(key)]) #always key[0]?
# print(enc)


#decode begins:
def rev_shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET  # Get the index of the character in ALPHABET2
	t2 = ord(k) - LOWERCASE_OFFSET   # Get the index of the key character
	return ALPHABET[(t1 - t2) % len(ALPHABET)]



key = ALPHABET[15] #0 to len.ALPHABET "af"
encoded = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac5"
print(f"len_encoded: {len(encoded)}")
print("---------------------------------------------------")

decoded_1 = ""
for i, c in enumerate(encoded):
	decoded_1 += rev_shift(c, key)
print(f"decoded_1: {decoded_1}")
print("decoded_2: ")
for i in range(0, len(decoded_1), 2):
	if i + 1 < len(decoded_1):
		first_i = ALPHABET.index(decoded_1[i])
		second_i = ALPHABET.index(decoded_1[i+1])
		res = first_i * 16 + second_i
		print(chr(res), end = '')

## to test

# encoded_short = "dcebc"
# for c in encoded_short:
# 	ascii_str += str(ord(c))
# print("str(ord(\"a\"))", int(ord("a")))
# print("str(ord(\"e\"))", int(ord("e")))

# ascii_str += str(ord("d"))
# ascii_str += str(ord("e"))
# print("ascii: ", ascii_str)


# ascii_str += str(ord("a"))
# print("ascii_str: ", ascii_str)
# decoded_2 += ascii_str
# print("decoded_2: ", decoded_2)



# decoded_2 =""
# decoded_2 = rev_b16_encode(decoded_1)
# print(f"decoded_2: {decoded_2}")

# (picoCTF{???????}) 
	 # dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac5