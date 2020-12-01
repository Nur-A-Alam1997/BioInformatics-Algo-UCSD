f=open("DBL.txt","r")


G={}
for l in f:
    p=((l.replace("->"," ").replace(":"," ").strip()).split())
    print(p[0],p[1],p[2])
    
#     print(l[0],l[3],l[5:])
    
    if p[0] not in G:
        G[p[0]]={}
        G[p[0]][p[1]]=int(p[2])
    if p[0] in G:
        G[p[0]][p[1]]=int(p[2])
        
for lines,v in (G.items()):
    print ("{",lines,":",v,"}")
    
for lines,v in (G.items()):
    for k,l in (v.items()):
        print ("{",k,":",l,"}")
    

print(type(G["5"]["3"]))



f.close()


