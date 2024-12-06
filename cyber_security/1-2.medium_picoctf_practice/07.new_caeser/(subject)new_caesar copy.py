import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(input):
	enc = ""
	for c in input:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	c_idx = ord(c) - LOWERCASE_OFFSET
	k_idx = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(c_idx + k_idx) % len(ALPHABET)] #len(ALPHABET) = 16

to_encode = "redacted"
key = "redacted"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

encoded_str = b16_encode(to_encode)
enc = ""
for i, c in enumerate(encoded_str):
	enc += shift(c, key[i % len(key)]) #always key[0]?
print(enc)


#We found a brand new type of encryption, 
# can you break the secret code? 
#(Wrap with picoCTF{}) 
# dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac