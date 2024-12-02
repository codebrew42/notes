#arr1 = "abcdefghijklmnopqrstuvwxyz"
#arr2 = "..s..t..z.....kb...y......"

input = "SYTe (eakdy tkd sjbyndr yar thjm) jdr j yobr kt skxbnyrd ersndzyo skxbryzyzkc. Skcyreyjcye jdr bdrercyrq gzya j ery kt sajhhrcmre gazsa yrey yarzd sdrjyzwzyo, yrsaczsjh (jcq mkkmhzcm) evzhhe, \
		jcq bdklhrx-ekhwzcm jlzhzyo. Sajhhrcmre nenjhho skwrd j cnxlrd kt sjyrmkdzre, jcq garc ekhwrq, rjsa ozrhqe j eydzcm (sjhhrq j thjm) gazsa ze enlxzyyrq yk jc kchzcr eskdzcm erdwzsr. \
		SYTe jdr j mdrjy gjo yk hrjdc j gzqr jddjo kt skxbnyrd ersndzyo evzhhe zc j ejtr, hrmjh rcwzdkcxrcy, jcq jdr akeyrq jcq bhjorq lo xjco ersndzyo mdknbe jdkncq yar gkdhq tkd tnc jcq bdjsyzsr. \
		Tkd yaze bdklhrx, yar thjm ze: bzskSYT{TD3UN3CSO_4774SV5_4D3_S001_7JJ384LS}"

print(input)

def	decode(input):
	arr1 = "abcdefghijklmnopqrstuvwxyz"
	arr2 = "jlsqrtmaz.vhxckb.deynwg.o." #fiup do not exist
	output = ""
	for chr in input:
		if not chr.isalpha():
			output += chr
		else:
			if chr in arr2:
				i = arr2.index(chr)
				output += arr1[i]
			elif chr.lower() in arr2:
				lowered_char = chr.lower()
				i = arr2.index(lowered_char)
				output += arr1[i].upper()
			else:
				output += "?"
	return (output)

output = decode(input)
print("output: ", output)