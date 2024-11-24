import base64
# Base64 encoded string
encoded_string = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzJhMnd6TW1zeWZRPT0nCg=="

# Decode the Base64 string
decoded_bytes = base64.b64decode(encoded_string)

# Convert bytes to a readable string (if possible)
try:
    decoded_string = decoded_bytes.decode('utf-8')
    print("Decoded string:", decoded_string)
except UnicodeDecodeError:
    print("The decoded data is not a UTF-8 string. It could be binary or encrypted.")
