import base64

s = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzJhMnd6TW1zeWZRPT0nCg=="


try:
	decoded_bytes = base64.b64decode(s)
	decoded_str = decoded_bytes.decode('utf-8')
	print(decoded_str)
except Exception as e:
	print(f"an error: {e}")


s2= "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg2a2wzMmsyfQ=="

decode1 = base64.b64decode(s2)
decode2 = decode1.decode('utf-8')
print(decode2)

arr2 = "..j..m..p......wxyza......"
arr3 = "wpjvJAM{jhlzhy_k3jy9wa3k_86kl32k2}"

def caeser(str):
	arr1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
	arr0 = ""
	for a in arr1:
		arr0 += a.upper()
	print(f'arr0: {arr0}')
	output = ""
	for c in str:
		if c in arr1:
			i = arr1.index(c)
			output += arr1[i+19]
		elif c in arr0:
			i = arr0.index(c)
			output += arr0[i+19]
		else:
			output += c
	return output

res = caeser(arr3)
print(res)