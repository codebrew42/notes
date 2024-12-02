import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

print("ALPHABET: ", ALPHABET)

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc


def b16_decode(bin):
	res = ""
	res = int(bin, 2)
	return res

def shift(c, k):
	t1 = ord(c) + LOWERCASE_OFFSET
	t2 = ord(k) + LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "givenstr"
key = "a"
assert all([k in ALPHABET for k in key])
assert len(key) == 1


enc = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"
print("encrypted: ", enc)

for i, c in enumerate(enc):
	enc += shift(c, key[i % len(key)])
dec = ""
dec = b16_decode(enc)

# (Wrap with picoCTF{}) 
# dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac