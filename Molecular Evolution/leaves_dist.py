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
        
        
# S={h:0 for h in G}        
# vis=[]
# q=[]
def dis(q):
    while q:
    #     for val in range(len(G)):
        z=str(q.pop(0))
        p=0
    #     print("all",z)
        if z not in vis:
            
    #         print("current",z)
            vis.append(str(z))
            
            for val in G[str(z)]:
                
                if val not in vis:
                    S[val]=S[z]+G[str(z)][val]
    #                 print("visited",vis)
                    q.extend(G[str(z)])
    #                 print("extended",q)
    return ['%02d' % float(v2) for k2,v2 in S.items() if len(G[k2])==1]


n=['%2d' % float(node) for node in G if len(G[node])==1]
print("      ",n)
# print(" ")
for nodes in G:
    if len(G[nodes])==1:
        S={h:0 for h in G}  
        vis=[]
        q=[]
        print(['%2d' % float(nodes)],dis([nodes]))



'''
for k,v in S.items() :
    
    print(v,sep=" ",end=" ")
 
       
    
            
'''