import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
ALPHABET2 = string.ascii_lowercase[:16] + string.ascii_lowercase[:16]
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

def shift(c, k):
	t1 = ord(c) + LOWERCASE_OFFSET
	t2 = ord(k) + LOWERCASE_OFFSET
	return ALPHABET[t1 + t2]

flag = "givenstr"
key = "a"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

def rev_shift(c, k):
	t1 = ord(c) + ord(c) + LOWERCASE_OFFSET
	t2 = ord(k) + LOWERCASE_OFFSET
	return ALPHABET[t1 - t2]

def rev_b16_encode(res):
	input = ""
	for c in res:

# (Wrap with picoCTF{}) 
# dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac