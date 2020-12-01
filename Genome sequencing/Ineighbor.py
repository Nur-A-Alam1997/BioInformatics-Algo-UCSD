from timeit import default_timer as timer

start = timer()

mot=set()
s="acgtacgacgatacggatacgaggatgacgagcatgacgatagcagatgacagtagcgactacgatgaaaaaaaaaaaaaaaatttccccccccccccccccaaaaattttttttaaaaaaaaaaaaccagacgatgacatagactacagatgacattg"
for i in range(len(s)):
    setg=["A","C","G","T"]
    
    Q=(s[:i]+setg[0]+s[i+1:]).upper()
    P=(s[:i]+setg[1]+s[i+1:]).upper()
    L=(s[:i]+setg[2]+s[i+1:]).upper()
    M=(s[:i]+setg[3]+s[i+1:]).upper()
    mot.add(Q)
    mot.add(P)
    mot.add(L)
    mot.add(M)
    
    
    
end = timer()
print( "Time in seconds",100*(end - start))