import	sys

def	hex_to_str(hex_str):
	hex_str = hex_str.replace(" ", "")
	bytes_read = bytes.fromhex(hex_str)
	return	bytes_read.decode('utf-8', 'ignore')

def	main():
	if len(sys.argv) != 2:
		print("argument is necessary")
		sys.exit(1)
	hex_input = sys.argv[1]

	res = hex_to_str(hex_input)
	print("converted: ", res)

if	__name__ == "__main__":
	main()
