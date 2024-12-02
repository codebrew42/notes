# base64

## what is base64?
- it's a way to encode binary data into a string of ASCII characters
- it's often used in web applications, such as encoding images or files

## how to determine if a string is base64 encoded?
- Character set: 0-9, A-Z, a-z, +, /, =
- Padding : the strings may end with one or two "="
- length : typically a multiple of 4 except the padding (example: 4*22= 88 characters)
-> why? because base64 encodes 24-bit data into 4 X 6-bit groups, so the length of the encoded string is a multiple of 4. If the data is not a multiple of 24 bits, padding("=") is added to make it so.

## example
- let's say we have a string: "hello"
- the ASCII code of "hello" is: 104 101 108 108 111
- then we can encode it into base64 by:
	- 104 -> 01101000
	- 101 -> 01100101
	- 108 -> 01101100
	- 108 -> 01101100
	- 111 -> 01101111
	- combined: 01101000 01100101 01101100 (24bit: set1) / 01101100 01101111 (16bit+padding: set2) 
- split into 6-bit groups: 011010 000110 100101 101100 / 011011 000110 1110
- add padding: 011010 000110 100101 101100 / 011011 000110 111000 (last 00 is padding)
	- they are 6-bit groups
- convert to base64: "aGVsbG8="
- so the base64 code of "hello" is: "aGVsbG8="

## why 64?
- because base64 uses 64 characters: 26 uppercase letters, 26 lowercase letters, 10 digits, and 2 special characters (+ and /)

## simple way to decode : base64 --decode (part of std library of linux, mac)
```bash
#invalid input (type: ')-> error
jin1@iMac-von-TJ 15.interencdec % echo "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg2a2wzMmsyfQ=='" | base64 --decode
base64: stdin: (null): error decoding base64 input stream 

#valid input -> decoded
jin1@iMac-von-TJ 15.interencdec % echo "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg2a2wzMmsyfQ==" | base64 --decode 
wpjvJAM{jhlzhy_k3jy9wa3k_86kl32k2}%
#-> then this can be decoded by caesar cypher with a shift of 7
```
