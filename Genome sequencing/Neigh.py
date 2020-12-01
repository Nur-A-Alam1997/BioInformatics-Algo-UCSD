from timeit import default_timer as timer

start = timer()

def ImmediateNeighbors(pat):
    
    neighbor=set()
    s=pat
#     s="acgtacgacgatacggatacgaggatgacgagcatgacgatagcagatgacagtagcgactacgatgaaaaaaaaaaaaaaaatttccccccccccccccccaaaaattttttttaaaaaaaaaaaaccagacgatgacatagactacagatgacattg"
    for i in range(len(s)):
        setg=["A","C","G","T"]
        
        Q=(s[:i]+setg[0]+s[i+1:])#.upper()
        P=(s[:i]+setg[1]+s[i+1:])#.upper()
        L=(s[:i]+setg[2]+s[i+1:])#.upper()
        M=(s[:i]+setg[3]+s[i+1:])#.upper()
        neighbor.add(Q)
        neighbor.add(P)
        neighbor.add(L)
        neighbor.add(M)
    return neighbor    
    

def Neighbors(pattern, d):
    if d == 0:
        return {pattern}
    ineighbor = ImmediateNeighbors(pattern)
    neighbor = ineighbor
    for j in range(d-1):
        for p in ineighbor:
            neighbor = neighbor.union(ImmediateNeighbors(p))
        ineighbor = neighbor
    return neighbor


if __name__ == "__main__":
    pattern="acgtacgacgatacggatacgaggatgacgagcatgacgatagcagatgacagtagcgactacgatgaaaaaaaaaaaaaaaatttccccccccccccccccaaaaattttttttaaaaaaaaaaaaccagacgatgacatagactacagatgacattgacgtacgacgatacggatacgaggatgacgagcatgacgatagcagatgacagtagcgactacgatgaaaaaaaaaaaaaaaatttccccccccccccccccaaaaattttttttaaaaaaaaaaaaccagacgatgacatagactacagatgacattg"
    print(sorted(Neighbors(pattern, 1)))
    

end = timer()
print( "Time in seconds",100*(end - start))
