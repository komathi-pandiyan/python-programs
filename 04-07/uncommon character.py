A="geeksforgeeks"
B="geeksquiz"
e=[]
string=""
for i in A:
    if (i not in B):
        if i not in e:
            e.append(i)
for i in B:
    if (i not in A):
        if i not in e:
            e.append(i)
e.sort()
if e!=[]:
    for i in range(len(e)):
        string+=e[i]
    print (string)
            
elif e==[]:
    print (-1)