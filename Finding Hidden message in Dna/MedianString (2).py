DNA=["CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC","GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC","GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG"]

# print(type(DNA),len(DNA[0]))

# Pattern="CGTGTAA"/33
# Pattern="AACGCTG"/25
# Pattern="ATAACGG"/39
Pattern="GAACCAC"
# Pattern="GGTTACT"#33
# Pattern="AATCCTA"

def hD(pat,seq):
	return len([ i for i in range(len(pat)) if pat[i] != seq[i]])



k=len(Pattern)
# print(k)
dis=0


bw=[]

for string in DNA:
	l=len(string)
	hd=float('inf')
	for i in range(l-k+1):
		CurHd=hD(Pattern,string[i:i+k])
		if CurHd<hd:
			hd=CurHd
			# print(hd)
			print(CurHd,string[i:i+k])
			bw.append(string[i:i+k])
			dis+=hd
		# print(dis)

print(dis,bw)
