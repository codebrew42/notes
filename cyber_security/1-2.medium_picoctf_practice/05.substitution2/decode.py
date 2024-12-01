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
res_dict['G'] = 'A'
res_dict['g'] = 'a'
res_dict['S'] = 'N'
res_dict['s'] = 'n'
res_dict['X'] = 'S'
res_dict['x'] = 's'
res_dict['D'] = 'H'
res_dict['d'] = 'h'
res_dict['N'] = 'R'
res_dict['n'] = 'r'
res_dict['W'] = 'd'
res_dict['w'] = 'd'

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

str = "vqkmKFL{G6D4U_4G41T515_15_73Y10A5_42JX1770}"
result = decode(str)
print(result)