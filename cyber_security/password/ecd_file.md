#.ecd file

## def
- file extension which indicates encrypted file
- commonly used by certain encryption software to denote files that have been encrypted to protect data

## how to open .ecd file
0. popular encryption prog : VeraCrypt, AxCrypt, openSSL, ...
1. figure out which prog was used 

	1-1. file filename.ecd :gather info

	1-2. analyze hex dum
	
		xxd level2.flag.txt.enc | head

- open the software that created that .ecd

- load the file
- provide the required p assword or key


## example : .txt.enc
	D^L^@Vw1%B@^WW^L\:V^HZ^BRWS:Z^N^DT^F^O^LT^^

### hint : presence of '^', ':', '@' 
- it might be an encoding scheme or a res of a simple encryption method like XOR

## common techniques to decrypt to consider
### XOR encryption
- you need a key to decrypt it
### Base64 encoding
	#python
	import base 64

	str = "..."

	try:
		decoded_bytes = base64.b64decode(str)
		decoded_str = decoded_bytes.decode('utf-8', 'ignore')
		print("decoded: ", decoded_str)
	except Exceptioon as e:
		print("not a valid base64 str")


### custom encoing