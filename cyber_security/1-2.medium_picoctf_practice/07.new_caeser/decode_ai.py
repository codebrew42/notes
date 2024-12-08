#ai_solved

import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def rev_shift(c, k):
    # Reverse the shift operation
    c_idx = ord(c) - LOWERCASE_OFFSET
    k_idx = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(c_idx - k_idx) % len(ALPHABET)]

def rev_b16_encode(encoded):
    # Convert pairs of characters back to original character
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

# The encoded message
encoded = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"

# Try all possible keys from ALPHABET
for possible_key in ALPHABET:
    try:
        # First reverse the shift cipher
        shifted_result = ""
        for c in encoded:
            shifted_result += rev_shift(c, possible_key)
        
        # Then reverse the b16 encoding
        final_result = rev_b16_encode(shifted_result)
        
        # Print if result contains printable ASCII
        if all(32 <= ord(c) <= 126 for c in final_result):
            print(f"Key '{possible_key}': picoCTF{{{final_result}}}")
    except:
        continue