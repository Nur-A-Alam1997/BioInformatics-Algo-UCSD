f=open("string recons.txt","r")
string=dict()
c=0
head=""
for lines in f:
    if len(lines)>1:
        head=(lines.strip())
        c+=1
        print(head,c)
   
# print(p)
# stringD={(lines.split())[0]:(lines.split())[1] for lines in f if len(lines)>1}

# print(stringD)

# head = filter(lambda x: x not in stringD.values(), stringD.keys())#[0]
# tail = filter(lambda x: x not in stringD.keys(), stringD.values())

# for vals,key in stringD.items() :
#     print(vals)
