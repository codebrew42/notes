

def dec(str, n):
	arr = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
	res = ""
	for c in str:
		i = arr.index(c)
		res += arr[i + n]
	print(res)



#s = "picoCTF{ynkooejcpdanqxeykjrbdofgkq}"
s = "ynkooejcpdanqxeykjrbdofgkq"
dec(s, 4)