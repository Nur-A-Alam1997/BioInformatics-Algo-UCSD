Motifs=[['T', 'C', 'G', 'G', 'G', 'G', 'g', 'T', 'T', 'T', 't', 't'], ['c', 'C', 'G', 'G', 't', 'G', 'A', 'c', 'T', 'T', 'a', 'C'], ['a', 'C', 'G', 'G', 'G', 'G', 'A', 'T', 'T', 'T', 't', 'C'], ['T', 't', 'G', 'G', 'G', 'G', 'A', 'c', 'T', 'T', 't', 't'], ['a', 'a', 'G', 'G', 'G', 'G', 'A', 'c', 'T', 'T', 'C', 'C'], ['T', 't', 'G', 'G', 'G', 'G', 'A', 'c', 'T', 'T', 'C', 'C'], ['T', 'C', 'G', 'G', 'G', 'G', 'A', 'T', 'T', 'c', 'a', 't'], ['T', 'C', 'G', 'G', 'G', 'G', 'A', 'T', 'T', 'c', 'C', 't'], ['T', 'a', 'G', 'G', 'G', 'G', 'A', 'a', 'c', 'T', 'a', 'C'], ['T', 'C', 'G', 'G', 'G', 't', 'A', 'T', 'a', 'a', 'C', 'C']]
print(Motifs)

count={symbol:[0 for i in range(12)] for symbol in "ACGT"}

for symbol,value in count.items():
	print(symbol,value)

print("")
print("")
print("")

for i in range(10):
	for j in range(12):
		symbol=Motifs[i][j].upper()
		count[symbol][j]+=1

print("")
print("")
print("")






for symbol,value in count.items():
	print(symbol,value)