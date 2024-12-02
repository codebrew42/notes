# File: notes.git/cyber_security/1-2.medium_picoctf_practice/07.new_caeser/decode_ai.py
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

def b16_decode(encoded):
    dec = ""
    for i in range(0, len(encoded), 2):
        # Get the indices of the two characters in ALPHABET
        index1 = ALPHABET.index(encoded[i])
        index2 = ALPHABET.index(encoded[i + 1])
        # Convert indices back to binary and then to character
        binary = "{0:04b}{1:04b}".format(index1, index2)
        dec += chr(int(binary, 2) + LOWERCASE_OFFSET)
    return dec

def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]

# Example usage
# Updated flag and key for decoding the specific string
encoded_string = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"
key = "c"  # Assuming the key remains the same for simplicity

# Decoding the encoded string
decoded_flag = b16_decode(encoded_string)
print("Decoded flag: ", decoded_flag)

# (Wrap with picoCTF{}) 