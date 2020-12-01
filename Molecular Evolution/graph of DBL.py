G = { "a" : ["c"],
      "b" : ["c", "e"],
      "c" : ["a", "b", "d", "e"],
      "d" : ["c"],
      "e" : ["c", "b"],
      "f" : []
    }
ul={v:0 for v in G}

def dist(G,s,t):
    q=[]
    vis=[]
    for val in G[s]:
#         if val==t:
#             break
        if val not in vis:
            q.extend(G[val])
#             ul[q]+=
            vis.append(val)
            q.pop(0)
            
            
            
print(dist(G,"a","d"))