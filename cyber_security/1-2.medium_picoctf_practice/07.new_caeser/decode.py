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



key = ALPHABET[1] #0 to len.ALPHABET
encoded = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac5"
decoded_1 = ""
for i, c in enumerate(encoded):
	decoded_1 += rev_shift(c, key)
print(f"decoded_1: {decoded_1}")
ascii_str = ""



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

#fix this!
def rev_b16_encode(encoded):
    # Process pairs of characters
    decoded = ""
    for i in range(0, len(encoded), 2):
        # Get indices of pair of characters
        first_idx = ALPHABET.index(encoded[i])
        second_idx = ALPHABET.index(encoded[i + 1])
        
        # Reconstruct the binary string
        binary = "{:04b}{:04b}".format(first_idx, second_idx)
        
        # Convert binary back to character
        decoded += chr(int(binary, 2))
    
    return decoded

decoded_2 =""
decoded_2 = rev_b16_encode(decoded_1)
print(f"decoded_2: {decoded_2}")

# (Wrap with picoCTF{}) 
# dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac5