f=open("DBL.txt","r")


G={}
for l in f:
    p=((l.replace("->"," ").replace(":"," ").strip()).split())
#     print(p[0],p[1],p[2])
    
#     print(l[0],l[3],l[5:])
    
    if p[0] not in G:
        G[p[0]]={}
        G[p[0]][p[1]]=int(p[2])
    if p[0] in G:
        G[p[0]][p[1]]=int(p[2])
"""        
for lines,v in (G.items()):
     print ("{",lines,":",v,"}")
    
for lines,v in (G.items()):
    
    for k,l in (v.items()):
         print ("{",k,":",l,"}")
    
print(type(G["5"]["3"]))

"""

f.close()




vis=[]
q=[0]

# G=["asd"]
# print(len(q))

##dfs
while q:
#     for val in range(len(G)):
    z=q.pop(0)
    print("all",z)
    if z not in vis:
        
        print("current",z)
        vis.append(str(z))
        print("visited",vis)
        q.extend(G[str(z)])
        print("extended",q)
            
