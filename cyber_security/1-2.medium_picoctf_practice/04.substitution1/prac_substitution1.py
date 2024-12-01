#arr1 = "abcdefghijklmnopqrstuvwxyz"

input = "SYTe (eakdy tkd sjbyndr yar thjm) jdr j yobr kt skxbnyrd ersndzyo skxbryzyzkc. Skcyreyjcye jdr bdrercyrq gzya j ery kt sajhhrcmre gazsa yrey yarzd sdrjyzwzyo, yrsaczsjh (jcq mkkmhzcm) evzhhe, jcq bdklhrx-ekhwzcm jlzhzyo. Sajhhrcmre nenjhho skwrd j cnxlrd kt sjyrmkdzre, jcq garc ekhwrq, rjsa ozrhqe j eydzcm (sjhhrq j thjm) gazsa ze enlxzyyrq yk jc kchzcr eskdzcm erdwzsr. SYTe jdr j mdrjy gjo yk hrjdc j gzqr jddjo kt skxbnyrd ersndzyo evzhhe zc j ejtr, hrmjh rcwzdkcxrcy, jcq jdr akeyrq jcq bhjorq lo xjco ersndzyo mdknbe jdkncq yar gkdhq tkd tnc jcq bdjsyzsr. Tkd yaze bdklhrx, yar thjm ze: bzskSYT{TD3UN3CSO_4774SV5_4D3_S001_7JJ384LS}"

def	frequency_attack(input):
	arr = []
	int = []
	dict = {}
	for char in input:
		if char.isalpha(): #if this char in arr1 exist
			dict[char] = dict.get(char, 0) + 1
	
	arr = list(dict.keys())
	int = list(dict.values())

	print("char: ", arr)
	print("valu: ", int)

	combined = sorted(zip(int, arr), reverse=True)  # {{ edit_1 }}

	int1, arr1 = zip(*combined)

	print("\nsorted char: ", arr1)
	print("\nsorted valu: ", int1)

frequency_attack(input)

def	decoded_list(arr1):
	dict = {}
	char = []
	for char in arr1:
		dict[char] = dict.get[]