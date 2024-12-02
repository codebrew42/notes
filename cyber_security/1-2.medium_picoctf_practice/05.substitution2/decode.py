def cal(input):
	char_count = {}  # Renamed from 'dict' to 'char_count'
	for char in input:
		if char in char_count:  # Updated variable name
			char_count[char] += 1
		else:
			char_count[char] = 1
	return(char_count)  # Updated return variable name

def sort(char_count):  # Updated parameter name
	# Sort the dictionary by value in descending order
	sorted_dict = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))  # Updated variable name
	return(sorted_dict)

input = "fnjdjjzqsfsjpjdxwmfnjdcjwwjsfxhwqsnjynqensknmmwkmuvafjdsjkadqftkmuvjfqfqmgsqgkwayqgekthjdvxfdqmfxgyaskthjdknxwwjgejfnjsjkmuvjfqfqmgslmkasvdquxdqwtmgstsfjusxyuqgqsfdxfqmglagyxujgfxwscnqknxdjpjdtasjlawxgyuxdojfxhwjsoqwwsnmcjpjdcjhjwqjpjfnjvdmvjdvadvmsjmlxnqensknmmwkmuvafjdsjkadqftkmuvjfqfqmgqsgmfmgwtfmfjxknpxwaxhwjsoqwwshafxwsmfmejfsfayjgfsqgfjdjsfjyqgxgyjzkqfjyxhmafkmuvafjdskqjgkjyjljgsqpjkmuvjfqfqmgsxdjmlfjgwxhmdqmasxllxqdsxgykmujymcgfmdaggqgeknjkowqsfsxgyjzjkafqgekmglqeskdqvfsmlljgsjmgfnjmfnjdnxgyqsnjxpqwtlmkasjymgjzvwmdxfqmgxgyquvdmpqsxfqmgxgymlfjgnxsjwjujgfsmlvwxtcjhjwqjpjxkmuvjfqfqmgfmaknqgemgfnjmlljgsqpjjwjujgfsmlkmuvafjdsjkadqftqsfnjdjlmdjxhjffjdpjnqkwjlmdfjknjpxgejwqsufmsfayjgfsqgxujdqkxgnqensknmmwsladfnjdcjhjwqjpjfnxfxgagyjdsfxgyqgemlmlljgsqpjfjkngqiajsqsjssjgfqxwlmdumagfqgexgjlljkfqpjyjljgsjxgyfnxffnjfmmwsxgykmglqeadxfqmglmkasjgkmagfjdjyqgyjljgsqpjkmuvjfqfqmgsymjsgmfwjxysfayjgfsfmogmcfnjqdjgjutxsjlljkfqpjwtxsfjxknqgefnjufmxkfqpjwtfnqgowqojxgxffxkojdvqkmkflqsxgmlljgsqpjwtmdqjgfjynqensknmmwkmuvafjdsjkadqftkmuvjfqfqmgfnxfsjjosfmejgjdxfjqgfjdjsfqgkmuvafjdskqjgkjxumgenqensknmmwjdsfjxknqgefnjujgmaenxhmafkmuvafjdsjkadqftfmvqiajfnjqdkadqmsqftumfqpxfqgefnjufmjzvwmdjmgfnjqdmcgxgyjgxhwqgefnjufmhjffjdyjljgyfnjqduxknqgjsfnjlwxeqsvqkmKFL{G6D4U_4G41T515_15_73Y10A5_42JX1770}"
char_dict = {}
char_dict = cal(input)

char_dict2 = {}
char_dict2 = sort(char_dict)
print(char_dict2)

res_dict = {}

#vqkmKFL
res_dict['v'] = 'p'
res_dict['q'] = 'i'
res_dict['k'] = 'c'
res_dict['m'] = 'o'
res_dict['K'] = 'C'
res_dict['F'] = 'T'
res_dict['L'] = 'F'

res_dict['V'] = 'P'
res_dict['Q'] = 'I'
res_dict['M'] = 'O'
res_dict['f'] = 't'
res_dict['l'] = 'f'

#assume
res_dict['J'] = 'E'
res_dict['j'] = 'e'
res_dict['F'] = 'T'
res_dict['f'] = 't'
res_dict['G'] = 'N'
res_dict['g'] = 'n'
res_dict['S'] = 'S'
res_dict['s'] = 's'
res_dict['X'] = 'A'
res_dict['x'] = 'a'
res_dict['D'] = ' '
res_dict['d'] = ' '
res_dict['N'] = 'H'
res_dict['n'] = 'h'
res_dict['W'] = 'L'
res_dict['w'] = 'l'
res_dict['P'] = 'V'
res_dict['p'] = 'v'
res_dict['I'] = 'Q'
res_dict['i'] = 'q'
res_dict['A'] = 'u'
res_dict['a'] = 'u'
res_dict['E'] = 'G'
res_dict['e'] = 'g'
res_dict['M'] = 'M'
res_dict['u'] = 'm'
res_dict['D'] = 'R'
res_dict['d'] = 'r'

res_dict['T'] = 'Y'
res_dict['t'] = 'y'
res_dict['Y'] = 'D'
res_dict['y'] = 'd'

res_dict['H'] = 'B'
res_dict['h'] = 'b'
res_dict['O'] = 'K'
res_dict['o'] = 'k'
def	add_notalpha(src, dest):
	for key in src:
		if key not in dest:
			if not key.isalpha():
				res_dict[key] = key
			else:
				res_dict[key] = '?'

add_notalpha(char_dict2, res_dict)
print("decoding map: ", res_dict)

def decode(input):
	input2 = input  # Simplified assignment
	output = ""  # Initialize output string
	for char in input2:
		if char in res_dict:  # Corrected condition
			output += res_dict[char]  # Use 'char' instead of 'key'
		else:
			output += char  # Keep the original character if not in res_dict
	return output  # Return the decoded output

def	check_successive(input):
	output = ""
	i = 0
	while i < len(input):
		if i < len(input) - 1 and input[i] == input[i + 1]:
			i += 2
		else:
			if input[i] not in output:
				output += input[i]
			i += 1
	return output

single_char = check_successive(input)
print("single: ", single_char)

str = "vqkmKFL{G6D4U_4G41T515_15_73Y10A5_42JX1770}"
result = decode(str)
print(result)

print("last str: ")
for chr in input:
	print(res_dict[chr], end='')
print()
