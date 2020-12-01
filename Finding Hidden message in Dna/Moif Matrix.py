Motifs=(""""

T C GGGG g TTT t t
c C G G t G A c T T a C
a C GGGG A TTT t C
T t GGGG A c T T t t
a a GGGG A c T T C C
T t GGGG A c T T C C
T C GGGG A T T cat
T C GGGG A T T c C t
T a GGGG A a c T a C
T C GGG t A T a a C C

""")
p=Motifs.split(" ")

l=''.join(p)


# #getting genome strings only
s=""
for i in l:
    
    if i in ("a,c,g,t,A,C,G,T"):
        
        s=s+i
print(s)            




##funtion
def lolo():
    return[0 for i in range(10)]
    
#         print(i)
       
    

