#1st way of defining
prog_dic = {
	123 : "number",
	"bug" : "an error in program ...",
	"func" : " a piece of code that you can call...",
	"loop" : "an action of doing ...",
}
print(prog_dic[123])
print(prog_dic["bug"])

#2nd way
prog_dic2 = {
	"bug" : 1,
	"func" : 3,
	"loop" : 5
}

print(prog_dic2["loop"])

#add element
prog_dic2["recursive"] = 0

print(f"print entire dict: ", prog_dic2)

#edit element
prog_dic2["recursive"] = 1
print(f"print added entire dict: ", prog_dic2)

#create an empty dic or clear out any dic
empty_dic = {}
print(f"empty: ", empty_dic)

#loop through a dict
for key in prog_dic:
	print("print key: ", key)
	print("print val: ", prog_dic[key])