def xor_decrypt(ciphertext, key):
    return bytes([b ^ key for b in ciphertext])

# Read the encrypted file
with open("level2.flag.txt.enc", "rb") as f:
    ciphertext = f.read()

# Try all possible single-byte keys
for key in range(256):
    decrypted = xor_decrypt(ciphertext, key)
    try:
        # Attempt to decode to UTF-8 and print
        print(f"Key: {key}, Decrypted: {decrypted.decode('utf-8', 'ignore')}")
    except Exception as e:
        # Ignore decode errors
        pass

