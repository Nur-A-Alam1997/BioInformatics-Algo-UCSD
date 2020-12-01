DNA=["AAATTGACGCAT","GACGACCACGTT","CGTCAGCGCCTG","GCTGAGCACCGG","AGTACGGGACAG"]

# print(type(DNA),len(DNA[0]))

Pattern="AAA"

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
