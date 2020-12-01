String="TCGGGGgTTTttcCGGtGAcTTaCaCGGGGATTTtCTtGGGGAcTTttaaGGGGAcTTCCTtGGGGAcTTCCTCGGGGATTcatTCGGGGATTcCtTaGGGGAacTaCTCGGGtATaaCC"
print(len(String))

Motif=[[0 for i in range(12)]for x in range(10)]


c=0
for i in range(10):
    for j in range(12):
        Motif[i][j]=String[c]
        c=c+1
        #print("its me:",c,"")


print(Motif)
print(" ")
print(" ")



for row  in Motif:
    print(row)

print("")