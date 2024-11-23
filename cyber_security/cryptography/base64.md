# base64

## what is base64?
- it's a way to encode binary data into a string of ASCII characters
- it's often used in web applications, such as encoding images or files

## example
- let's say we have a string: "hello"
- the ASCII code of "hello" is: 104 101 108 108 111
- then we can encode it into base64 by:
	- 104 -> 01101000
	- 101 -> 01100101
	- 108 -> 01101100
	- 108 -> 01101100
	- 111 -> 01101111
	- combined: 01101000 01100101 01101100 01101100 01101111
	- split into 6-bit groups: 011010 000110 100101 101100 011011 000110 1110
	- add padding: 011010 000110 100101 101100 011011 000110 111000
	- convert to base64: "aGVsbG8="
- so the base64 code of "hello" is: "aGVsbG8="

## why 64?
- because base64 uses 64 characters: 26 uppercase letters, 26 lowercase letters, 10 digits, and 2 special characters (+ and /)

## simple way to decode
```bash
#invalid input -> error
jin1@iMac-von-TJ 15.interencdec % echo "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg2a2wzMmsyfQ=='" | base64 --decode
base64: stdin: (null): error decoding base64 input stream 

#valid input -> decoded
jin1@iMac-von-TJ 15.interencdec % echo "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg2a2wzMmsyfQ==" | base64 --decode 
wpjvJAM{jhlzhy_k3jy9wa3k_86kl32k2}%
#-> then this can be decoded by caesar cypher with a shift of 7
```
