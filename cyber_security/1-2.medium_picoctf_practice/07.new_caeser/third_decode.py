import string

LOW_OFFSET = ord("a")
ALPHA = string.ascii_lowercase[:16] #ALPHA = "abcd...p"

def		b16_encode(input): #"a"
	enc = ""
	for c in input:
		binary = "{0:08b}".format(ord(c)) #ord("a") = 97 = 0110 0001
		enc += ALPHA[int(binary[:4], 2)] #"g"
		enc += ALPHA[int(binary[4:], 2)] #"b"
	return enc #gb

def		shift(str, k): #"b" = 1 
	res = ""
	idx_k = ord(k) - LOW_OFFSET
	for c in str:
		idx_c = ord(c) - LOW_OFFSET
		res += ALPHA[(idx_c + idx_k) % len(ALPHA)]
	return res #"hc"

#to test : properly encoded
print(shift(b16_encode("a"), "p"))



#We found a brand new type of encryption, 
# can you break the secret code? 
#(Wrap with picoCTF{}) 
encoded = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"
print(f"encoded: {encoded}")

#to decode
def		rev_shift(str, k):
	res = ""
	idx_k = ord(k) - LOW_OFFSET
	for c in str:
		idx_c = ord(c) - LOW_OFFSET
		res += ALPHA[(idx_c - idx_k) % len(ALPHA)]
	return res

key = "e"
rev_shifted = rev_shift(encoded, key)
print(f"rev_shifted with the key \"{key}\": \n{rev_shifted}")

def		rev_b16_encode(input):
	res = ""
	print("rev: ")
	for i in range(0, len(input), 2):
		fi = ALPHA.index(input[i])
		se = ALPHA.index(input[i + 1])
		ch = "{0:04b}{1:04b}".format(fi, se)
		n = int(ch, 2)
		print(f"{{{ch} -> {n}}}")
		#print(n, end="")
		res += chr(n)
	return res
		# ch_to_int = int(ch, 2)
		# res += ALPHA[ch_to_int]

rev_encoded = rev_b16_encode(rev_shifted)
print(f"(in: \"{rev_shifted}\") \n -> out: \"{rev_encoded}\" ")