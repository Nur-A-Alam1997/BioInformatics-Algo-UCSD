from timeit import default_timer as timer

start = timer()
s="acgtacgacgatacggatacgaggatgacgagcatgacgatagcagatgacagtagcgactacgatgaaaaaaaaaaaaaaaatttccccccccccccccccaaaaattttttttaaaaaaaaaaaaccagacgatgacatagactacagatgacattg"


def ImmediateNeighbors(pattern):
    neighbor = set()
    nset = {'A', 'C', 'G', 'T'}
    for i in range(len(pattern)):
        for n in nset:
            neighbor.add(pattern[:i]+n+pattern[i+1:])
    return neighbor

print((sorted(ImmediateNeighbors(s))))

end = timer()
print( ("Time in seconds",100*(end - start)))