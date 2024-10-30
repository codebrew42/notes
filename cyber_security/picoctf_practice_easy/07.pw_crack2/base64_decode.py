import base64

# Replace this string with your Base64-encoded text
encoded_string = "D^L^@Vw1%B@^WW^L\\:V^HZ^BRWS:Z^N^DT^F^O^LT^^"

# Attempt to decode the Base64 string
try:
    # Decode the Base64 string
    decoded_bytes = base64.b64decode(encoded_string)
    # Convert bytes to string
    decoded_string = decoded_bytes.decode('utf-8', 'ignore')
    print("Decoded String:", decoded_string)
except Exception as e:
    print("Error during decoding:", e)

