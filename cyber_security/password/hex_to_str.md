# example 1 : pico_easy: get pw2

	jin1@iMac-von-TJ 07.pw_crack2 % vim 07.level2.py 

	### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
	def str_xor(secret, key):
		#extend key to secret length
		new_key = key
		i = 0
		while len(new_key) < len(secret):
			new_key = new_key + key[i]
			i = (i + 1) % len(key)
		return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
	###############################################################################

	flag_enc = open('level2.flag.txt.enc', 'rb').read()



	def level_2_pw_check():
		user_pw = input("Please enter correct password for flag: ")
		if( user_pw == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) ):
			print("Welcome back... your flag, user:")
			decryption = str_xor(flag_enc.decode(), user_pw)
			print(decryption)
			return
		print("That password is incorrect")



	level_2_pw_check()
	~                                   

- look at the : if ...

## convert : hex_to_str
	def hex_to_str(hex_str):
		hex_str = hex_str.replace(" ", "") #rm space
		hex_to_bytes = bytes.fromhex(hex_str)
		return hex_to_bytes_decode('utf-8', 'ignore') #convert bytes -> str, ignore any bytes cannt be decoded/not valid UTF-8