import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
#ALPHABET = "abcdefg..p" [0] - [15] = 16개

def b16_encode(input): #
	enc = ""
	for c in input:
		binary = "{0:08b}".format(ord(c)) #0111 1101
		enc += ALPHABET[int(binary[:4], 2)] #ret = "0111" -> set[0111 = 7] => h
		enc += ALPHABET[int(binary[4:], 2)] #ret = "1101" -> set[13] => n
	return enc # "hn"

def shift(c, k):
	c_idx = ord(c) - LOWERCASE_OFFSET
	k_idx = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(c_idx + k_idx) % len(ALPHABET)] #len(ALPHABET) = 16

to_encode = "redacted"
key = "a" #"a"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

encoded_str = b16_encode(to_encode)
enc = ""
for i, c in enumerate(encoded_str):
	enc += shift(c, key[i % len(key)]) #always key[0]?


#We found a brand new type of encryption, 
# can you break the secret code? 
#(Wrap with picoCTF{}) 
decoded = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"
print(f"decoded: {decoded}")
def rev_shift(str, i):
	res = ""
	k_idx = ord(ALPHABET[i]) - LOWERCASE_OFFSET
	for c in str:
		c_idx = ord(c) - LOWERCASE_OFFSET
		new = ALPHABET[(c_idx - k_idx) % len(ALPHABET)]
		res += new
	return (res)



def build_char(str):
	dest = ""
	for i in range(0, len(str), 2):
		first = ALPHABET.index(str[i])
		second = ALPHABET.index(str[i+1])
		res = "{0:04b}{1:04b}".format(first, second)
		res_to_int = int(res, 2)
		int_to_chr = chr(res_to_int)
		dest += int_to_chr
	return dest

def str_printable(str):
	for c in str:
		if ord(c) >=32 and ord(c) <=126:
			continue
		elif c == str[len(str) - 1]:
			return 1
		else:
			return 0

def print_only_printable(decoded):
	if str_printable(decoded) == 0:
		print ("decoded: not printable")
		return
	for i in range(len(ALPHABET)):
		rev_shifted = rev_shift(decoded, i)
		print(f"rev_shifted: {rev_shifted}")
		chars_built = build_char(rev_shifted)
		if str_printable(decoded) == 0:
			print ("chars_built: not printable")
			return
		print(f"key_idx: {i}, build_chars: {chars_built}")

print_only_printable(decoded)